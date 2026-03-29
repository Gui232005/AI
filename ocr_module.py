import re
import cv2
import numpy as np
from paddleocr import PaddleOCR

DEBUG = False

# Padrões de matrícula em portugal em REGEX
PLATE_PATTERN = re.compile(
    r'\b([A-Z]{2}[-\s]?\d{2}[-\s]?[A-Z]{2}|'   # AA-00-AA
    r'\d{2}[-\s]?[A-Z]{2}[-\s]?\d{2}|'          # 00-AA-00
    r'[A-Z]{2}[-\s]?\d{2}[-\s]?\d{2}|'          # AA-00-00
    r'\d{2}[-\s]?\d{2}[-\s]?[A-Z]{2})\b',        # 00-00-AA
    re.IGNORECASE,
)

def _debug_show(title: str, image: np.ndarray) -> None:
    """Mostra uma janela com a imagem se DEBUG=True. Fecha com qualquer tecla."""
    if not DEBUG:
        return
    cv2.imshow(title, image)
    print(f"[DEBUG] {title} — pressiona qualquer tecla para continuar...")
    cv2.waitKey(0)
    cv2.destroyWindow(title)


class LicensePlateOCR:
    def __init__(self, lang: str = "en", use_gpu: bool = True):
        """
        Inicializa o PaddleOCR optimizado para leitura de matrículas.

        Args:
            lang: Idioma do modelo OCR ('en' cobre caracteres alfanuméricos).
            use_gpu: Usa GPU se disponível.
        """
        self.ocr = PaddleOCR(
            use_textline_orientation=True,
            lang=lang,
            device="gpu" if use_gpu else "cpu",
        )

    # Pré-processamento
    def _preprocess(self, image: np.ndarray) -> np.ndarray:
        """Converte para escala de cinza e preto e aumenta o contraste e binariza."""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
        _debug_show("DEBUG: Original", image)
        _debug_show("DEBUG: Cinza", gray)

        # CLAHE para equalização local de histograma
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(gray)
        _debug_show("DEBUG: CLAHE (contraste)", enhanced)

        # Binarização adaptativa
        binary = cv2.adaptiveThreshold(
            enhanced, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY, 11, 2,
        )
        _debug_show("DEBUG: Binarizado", binary)

        # Volta para BGR para o PaddleOCR
        return cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)

    # Leitura
    def read_image(self, image: np.ndarray, preprocess: bool = True) -> list[dict]:
        """
        Executa OCR numa imagem (numpy array BGR).

        Args:
            image: Imagem no formato OpenCV (BGR).
            preprocess: Aplicar pré-processamento antes do OCR.

        Returns:
            Lista de dicts com 'text', 'confidence' e 'bbox'.
        """
        img = self._preprocess(image) if preprocess else image
        results = list(self.ocr.predict(img))
        detections = []
        for res in results:
            polys = res.get("rec_polys", [])
            texts = res.get("rec_texts", [])
            scores = res.get("rec_scores", [])
            for bbox, text, score in zip(polys, texts, scores):
                detections.append({
                    "text": text.strip().upper(),
                    "confidence": round(float(score), 4),
                    "bbox": bbox.tolist() if hasattr(bbox, "tolist") else bbox,
                })

        if DEBUG:
            debug_img = image.copy()
            for det in detections:
                pts = np.array(det["bbox"], dtype=np.int32)
                cv2.polylines(debug_img, [pts], isClosed=True, color=(255, 165, 0), thickness=2)
                origin = (pts[0][0], pts[0][1] - 8)
                cv2.putText(
                    debug_img,
                    f"{det['text']} ({det['confidence']:.0%})",
                    origin,
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 165, 0),
                    2,
                )
            _debug_show("DEBUG: Todas as detecções OCR (laranja)", debug_img)

        return detections

    def read_file(self, path: str, preprocess: bool = True) -> list[dict]:
        """
        Executa OCR num ficheiro de imagem.

        Args:
            path: Caminho para a imagem (JPEG, PNG, etc.).
            preprocess: Aplicar pré-processamento.

        Returns:
            Lista de dicts com 'text', 'confidence' e 'bbox'.
        """
        if preprocess:
            image = cv2.imread(path)
            if image is None:
                raise FileNotFoundError(f"Não foi possível abrir a imagem: {path}")
            return self.read_image(image, preprocess=True)
        # Sem pré-processamento: passa o path directamente ao PaddleOCR
        results = list(self.ocr.predict(path))
        detections = []
        for res in results:
            for bbox, text, score in zip(
                res.get("rec_polys", []),
                res.get("rec_texts", []),
                res.get("rec_scores", []),
            ):
                detections.append({
                    "text": text.strip().upper(),
                    "confidence": round(float(score), 4),
                    "bbox": bbox.tolist() if hasattr(bbox, "tolist") else bbox,
                })
        return detections

    # Extracção da matrícula
    def extract_plates(
        self,
        image_or_path,
        preprocess: bool = True,
        min_confidence: float = 0.6, # minimo de 60% de conficanca
    ) -> list[dict]:
        """
        Detecta e filtra textos que correspondem a padrões de matrícula.

        Args:
            image_or_path: numpy array (BGR) ou caminho para ficheiro.
            preprocess: Aplicar pré-processamento.
            min_confidence: Confiança mínima para incluir resultado.

        Returns:
            Lista de dicts com 'plate', 'confidence' e 'bbox'.
        """
        if isinstance(image_or_path, str):
            original = cv2.imread(image_or_path)
            detections = self.read_file(image_or_path, preprocess=preprocess)
        else:
            original = image_or_path
            detections = self.read_image(image_or_path, preprocess=preprocess)

        plates = []
        for det in detections:
            if det["confidence"] < min_confidence:
                continue
            match = PLATE_PATTERN.search(det["text"])
            if match:
                plates.append({
                    "plate": _normalize_plate(match.group()),
                    "raw": det["text"],
                    "confidence": det["confidence"],
                    "bbox": det["bbox"],
                })

        if DEBUG and original is not None:
            annotated = draw_plates(original, plates)
            _debug_show("DEBUG: Matrículas detectadas (verde)", annotated)
            print(f"[DEBUG] {len(plates)} matrícula(s) encontrada(s):")
            for p in plates:
                print(f"  {p['plate']}  conf={p['confidence']:.1%}  bbox={p['bbox']}")

        return plates


# helpers
def _normalize_plate(text: str) -> str:
    """Remover espaços, converter para maiúsculas e garante hífens."""
    clean = re.sub(r"[\s]", "-", text.strip().upper())
    # Colapsa hífens múltiplos
    clean = re.sub(r"-{2,}", "-", clean)
    return clean


def draw_plates(image: np.ndarray, plates: list[dict]) -> np.ndarray:
    """
    Desenha as bounding boxes e o texto das matrículas na imagem.

    Args:
        image: Imagem original (BGR).
        plates: Lista de resultados de extract_plates().

    Returns:
        Imagem anotada.
    """
    output = image.copy()
    for p in plates:
        pts = np.array(p["bbox"], dtype=np.int32)
        cv2.polylines(output, [pts], isClosed=True, color=(0, 255, 0), thickness=2)
        origin = (pts[0][0], pts[0][1] - 10)
        cv2.putText(
            output,
            f"{p['plate']} ({p['confidence']:.0%})",
            origin,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2,
        )
    return output

# Uso directo no terminal, APENAS PARA DEBUG!
if __name__ == "__main__":
    import sys
    ocr = LicensePlateOCR()

    for path in sys.argv[1:]:
        print(f"\n=== {path} ===")
        try:
            plates = ocr.extract_plates(path)
            if plates:
                for p in plates:
                    print(f"  Matrícula : {p['plate']}")
                    print(f"  Confiança : {p['confidence']:.1%}")
            else:
                print("  Nenhuma matrícula detectada.")
        except FileNotFoundError as e:
            print(f"  ERRO: {e}")
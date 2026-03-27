import os

os.system('cls' if os.name == 'nt' else 'clear')

<<<<<<< HEAD


from rede import linha_reta, origem_faro, cidades
# Vamos precisar de importar a função de OCR que vais criar
# from ocr_module import extrair_matricula 
=======
from rede import linha_reta, origem_faro, cidades
from ocr_module import LicensePlateOCR
>>>>>>> 1de076472bf381b97e931ffc6b1876ab00f8d400

def limpar_ecra():
    os.system('cls' if os.name == 'nt' else 'clear')

<<<<<<< HEAD
def menu_principal(matricula):
    limpar_ecra()
    print(f"--- BEM-VINDO: {matricula} ---")
    print("1. Procurar Caminho (Custo Uniforme)")
    print("2. Procurar Caminho (Profundidade Limitada)")
    print("3. Procurar Caminho (Sôfrega)")
    print("4. Procurar Caminho (A*)")
    print("0. Sair")
    
    #os.system('cls' if os.name == 'nt' else 'clear')
    
    # Aqui o teu colega depois insere a lógica das escolhas
    input("\nPressione Enter para continuar...")

def login():
    limpar_ecra()
    print("--- LOGIN DO SISTEMA (OCR) ---")
    
    # Exemplo de como funcionará:
    # caminho_imagem = "Seat-Ibiza-FR-8-scaled_925x520_acf_cropped..."
    # matricula_detectada = extrair_matricula(caminho_imagem)
    
    matricula_detectada = "00-AA-00" # Placeholder enquanto não temos o OCR
    
    if matricula_detectada:
        print(f"Matrícula detectada com sucesso: {matricula_detectada}")
        input("Acesso garantido. Pressione Enter para entrar no menu...")
        menu_principal(matricula_detectada)
    else:
        print("Erro: Não foi possível ler a matrícula.")
=======
def escolher_cidade(prompt):
    cidades_lista = sorted(cidades.keys())
    print(f"\n{prompt}")
    for i, c in enumerate(cidades_lista, 1):
        print(f"  {i:2}. {c}")
    while True:
        entrada = input("Número ou nome: ").strip()
        if entrada.isdigit() and 1 <= int(entrada) <= len(cidades_lista):
            return cidades_lista[int(entrada) - 1]
        elif entrada.title() in cidades:
            return entrada.title()
        else:
            print("Cidade inválida, tenta de novo.")

def menu_principal(matricula, origem, destino):
    while True:
        limpar_ecra()
        print(f"--- BEM-VINDO: {matricula} ---")
        print(f"Percurso: {origem}  →  {destino}\n")
        print("1. Procurar Caminho (Custo Uniforme)")
        print("2. Procurar Caminho (Profundidade Limitada)")
        print("3. Procurar Caminho (Sôfrega)")
        print("4. Procurar Caminho (A*)")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "0":
            print("A sair...")
            break
        elif opcao in ("1", "2", "3", "4"):
            # Os algoritmos serão implementados pelos colegas
            print(f"\n[TODO] Algoritmo {opcao} — {origem} → {destino}")
            input("\nPressione Enter para continuar...")
        else:
            input("Opção inválida. Pressione Enter para tentar de novo...")

def login():
    limpar_ecra()
    print("--- LOGIN DO SISTEMA (OCR) ---\n")

    caminho_imagem = input("Caminho para a imagem da matrícula: ").strip()

    if not os.path.isfile(caminho_imagem):
        print(f"Erro: ficheiro não encontrado — {caminho_imagem}")
        return

    print("\nA processar imagem com OCR...")
    ocr = LicensePlateOCR()
    plates = ocr.extract_plates(caminho_imagem)

    if not plates:
        print("Erro: Não foi possível detectar nenhuma matrícula na imagem.")
        return

    # Usa a matrícula com maior confiança
    melhor = max(plates, key=lambda p: p["confidence"])
    matricula_detectada = melhor["plate"]

    print(f"\nMatrícula detectada: {matricula_detectada}  (confiança: {melhor['confidence']:.1%})")
    print("Acesso garantido!\n")

    origem = escolher_cidade("Cidade de origem:")
    destino = escolher_cidade("Cidade de destino:")

    input(f"\nPercurso definido: {origem} → {destino}\nPressione Enter para entrar no menu...")
    menu_principal(matricula_detectada, origem, destino)
>>>>>>> 1de076472bf381b97e931ffc6b1876ab00f8d400

if __name__ == "__main__":
    login()




# Testar o método de Haversine
distancia_teste = linha_reta('Viseu', 'Faro')
print(f"Linha reta Viseu-Faro: {distancia_teste} km")

# Testar a tabela fixa para Faro (Tabela 2)
distancia_faro = origem_faro['Viseu']
print(f"Tabela fixa Viseu-Faro: {distancia_faro} km")
<<<<<<< HEAD

=======
>>>>>>> 1de076472bf381b97e931ffc6b1876ab00f8d400

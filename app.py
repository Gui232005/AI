import os
import json
import tempfile
from datetime import datetime

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

from rede import cidades, coordenadas, linha_reta
from ocr_module import LicensePlateOCR, GPU_DISPONIVEL
from search_algorithms.uniformCostSearch import uniform_cost_search
from search_algorithms.depthLimitedSearch import depth_limited_search
from search_algorithms.greedyBestFirstSearch import greedyBest_FirstSearch
from search_algorithms.A import a_star_search
from local_llm.LocalLLM import LocalLLM

HISTORICO_FILE = os.path.join(os.path.dirname(__file__), "historico.json")
CIDADES_SORTED = sorted(cidades.keys())


# ── Persistence ───────────────────────────────────────────────────────────────

def carregar_historico() -> list:
    if os.path.exists(HISTORICO_FILE):
        with open(HISTORICO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def guardar_historico(historico: list) -> None:
    with open(HISTORICO_FILE, "w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, indent=2)


def registar_viagem(matricula, algoritmo, origem, destino, caminho, distancia):
    entrada = {
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "matricula": matricula,
        "algoritmo": algoritmo,
        "origem": origem,
        "destino": destino,
        "caminho": " → ".join(caminho),
        "distancia": distancia,
    }
    st.session_state.historico.append(entrada)
    guardar_historico(st.session_state.historico)


# ── Session state ─────────────────────────────────────────────────────────────

def init_session_state():
    defaults = {
        "autenticado": False,
        "matricula": "",
        "ultimo_resultado": None,
        "historico": None,
        "llm_cache": {},
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
    if st.session_state.historico is None:
        st.session_state.historico = carregar_historico()


# ── OCR — loaded once per session ─────────────────────────────────────────────

@st.cache_resource
def get_ocr(use_gpu: bool) -> LicensePlateOCR:
    return LicensePlateOCR(use_gpu=use_gpu)


# ── Interactive map ───────────────────────────────────────────────────────────

def build_folium_map(highlight_path: tuple = None):
    # Bounds of continental Portugal
    pt_bounds = [[36.9, -9.6], [42.2, -6.1]]

    m = folium.Map(
        location=[39.6, -8.0],
        zoom_start=7,
        tiles="CartoDB Positron",
        min_zoom=6,
        max_bounds=True,
    )
    m.fit_bounds(pt_bounds)

    # Build edge set for highlight detection
    highlight_set = set()
    if highlight_path and len(highlight_path) > 1:
        for i in range(len(highlight_path) - 1):
            highlight_set.add((highlight_path[i], highlight_path[i + 1]))
            highlight_set.add((highlight_path[i + 1], highlight_path[i]))

    # Draw all connections (base edges) as thin grey lines
    drawn = set()
    for cidade, vizinhos in cidades.items():
        for vizinho, distancia in vizinhos.items():
            edge = tuple(sorted([cidade, vizinho]))
            if edge in drawn or (cidade, vizinho) in highlight_set:
                continue
            drawn.add(edge)
            folium.PolyLine(
                [[coordenadas[cidade][0], coordenadas[cidade][1]],
                 [coordenadas[vizinho][0], coordenadas[vizinho][1]]],
                color="#b0bec5", weight=2, opacity=0.4,
            ).add_to(m)

    # Draw route as bold blue line with distance labels
    if highlight_path and len(highlight_path) > 1:
        route_coords = [
            [coordenadas[c][0], coordenadas[c][1]] for c in highlight_path
        ]
        folium.PolyLine(
            route_coords, color="#3b82f6", weight=6, opacity=0.9,
        ).add_to(m)

        # Distance labels centered on each segment
        for i in range(len(highlight_path) - 1):
            u, v = highlight_path[i], highlight_path[i + 1]
            mid_lat = (coordenadas[u][0] + coordenadas[v][0]) / 2
            mid_lon = (coordenadas[u][1] + coordenadas[v][1]) / 2
            dist = cidades[u][v]
            label_html = (
                f'<div style="background:#fff;border:1px solid #3b82f6;'
                f'border-radius:12px;padding:2px 8px;font-size:11px;'
                f'font-weight:600;color:#1e40af;white-space:nowrap;'
                f'box-shadow:0 1px 4px rgba(0,0,0,0.15);'
                f'text-align:center">'
                f'{dist} km</div>'
            )
            folium.Marker(
                [mid_lat, mid_lon],
                icon=folium.DivIcon(
                    html=label_html,
                    icon_size=(70, 22),
                    icon_anchor=(35, 11),
                ),
            ).add_to(m)

    # City markers
    for city, (lat, lon) in coordenadas.items():
        is_on_route = highlight_path and city in highlight_path
        is_start = highlight_path and city == highlight_path[0]
        is_end = highlight_path and city == highlight_path[-1]

        if is_start:
            icon_color, icon_str, prefix = "green", "play", "fa"
        elif is_end:
            icon_color, icon_str, prefix = "red", "flag-checkered", "fa"
        elif is_on_route:
            icon_color, icon_str, prefix = "blue", "circle", "fa"
        else:
            icon_color, icon_str, prefix = "gray", "circle", "fa"

        popup_html = f"<b>{city}</b>"
        if is_on_route:
            idx = list(highlight_path).index(city)
            popup_html += f"<br>Paragem {idx + 1} de {len(highlight_path)}"

        folium.Marker(
            [lat, lon],
            popup=folium.Popup(popup_html, max_width=200),
            tooltip=city,
            icon=folium.Icon(color=icon_color, icon=icon_str, prefix=prefix),
        ).add_to(m)

    return m


# ── Sidebar — OCR login ───────────────────────────────────────────────────────

def render_sidebar_login():
    st.sidebar.title("🔐 Autenticação")

    if st.session_state.autenticado:
        st.sidebar.success(f"Matrícula: **{st.session_state.matricula}**")
        if st.sidebar.button("Terminar sessão"):
            st.session_state.autenticado = False
            st.session_state.matricula = ""
            st.session_state.ultimo_resultado = None
            st.rerun()
        return

    use_gpu = False
    if GPU_DISPONIVEL:
        use_gpu = st.sidebar.checkbox("Usar GPU para OCR", value=True)

    uploaded = st.sidebar.file_uploader(
        "Foto da matrícula", type=["png", "jpg", "jpeg"]
    )

    if uploaded is not None:
        st.sidebar.image(uploaded, caption="Imagem carregada", use_container_width=True)
        if st.sidebar.button("Autenticar", type="primary"):
            tmp = None
            try:
                suffix = os.path.splitext(uploaded.name)[1] or ".jpg"
                with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as f:
                    f.write(uploaded.read())
                    tmp = f.name

                with st.sidebar.spinner("A processar OCR..."):
                    ocr = get_ocr(use_gpu)
                    plates = ocr.extract_plates(tmp)

                if plates:
                    best = max(plates, key=lambda p: p["confidence"])
                    st.session_state.matricula = best["plate"]
                    st.session_state.autenticado = True
                    st.rerun()
                else:
                    st.sidebar.error(
                        "Nenhuma matrícula detectada. Tenta com outra imagem."
                    )
            finally:
                if tmp and os.path.exists(tmp):
                    os.unlink(tmp)


# ── Tab 1: City map ───────────────────────────────────────────────────────────

def render_tab_mapa():
    st.header("Mapa da Rede de Cidades")

    highlight = None
    if st.session_state.ultimo_resultado:
        highlight = tuple(st.session_state.ultimo_resultado["caminho"])

    mapa = build_folium_map(highlight_path=highlight)
    st_folium(mapa, use_container_width=True, height=600)

    if highlight:
        res = st.session_state.ultimo_resultado
        cols = st.columns(3)
        cols[0].metric("Rota", f"{res['caminho'][0]} → {res['caminho'][-1]}")
        cols[1].metric("Distância", f"{res['distancia']} km")
        cols[2].metric("Algoritmo", res["algoritmo"].split("(")[0].strip())


# ── Tab 2: Route planning ─────────────────────────────────────────────────────

def render_tab_rota():
    if not st.session_state.autenticado:
        st.warning("Faz login na barra lateral para planear uma rota.")
        return

    st.header("Planear Rota")

    col1, col2 = st.columns(2)
    with col1:
        origem = st.selectbox("Cidade de Origem", CIDADES_SORTED, key="origem_sel")
    with col2:
        destino_options = [c for c in CIDADES_SORTED if c != origem]
        destino = st.selectbox("Cidade de Destino", destino_options, key="destino_sel")

    algoritmo = st.radio(
        "Algoritmo de Pesquisa",
        ["Custo Uniforme (UCS)", "Profundidade Limitada (DLS)", "Sôfrega (Greedy)", "A*"],
        horizontal=True,
    )

    limite = 5
    if "DLS" in algoritmo:
        limite = st.number_input(
            "Limite de Profundidade", min_value=1, max_value=30, value=5
        )

    if st.button("Calcular Rota", type="primary"):
        with st.spinner("A calcular rota..."):
            resultado = _calcular_rota(origem, destino, algoritmo, int(limite))

        if resultado is None:
            st.error("Não foi possível encontrar um caminho entre as cidades seleccionadas.")
        elif isinstance(resultado, str):
            st.warning(
                f"Pesquisa terminada com: **{resultado}**. "
                "Tenta aumentar o limite de profundidade."
            )
        else:
            caminho, distancia = resultado
            st.session_state.ultimo_resultado = {
                "algoritmo": algoritmo,
                "caminho": caminho,
                "distancia": distancia,
            }
            registar_viagem(
                st.session_state.matricula,
                algoritmo, origem, destino, caminho, distancia,
            )
            st.rerun()

    # Always show the last result
    if st.session_state.ultimo_resultado:
        res = st.session_state.ultimo_resultado
        st.divider()
        st.subheader("Último resultado")
        st.success(f"**{' → '.join(res['caminho'])}**")
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("Distância", f"{res['distancia']} km")
        col_b.metric("Cidades", len(res["caminho"]))
        col_c.metric("Algoritmo", res["algoritmo"].split("(")[0].strip())


def _calcular_rota(origem, destino, algoritmo, limite):
    if "UCS" in algoritmo:
        result = uniform_cost_search(cidades, origem, destino)
        if result is None:
            return None
        cost, path = result
        return path, cost

    elif "DLS" in algoritmo:
        result = depth_limited_search(origem, destino, cidades, limite)
        if isinstance(result, str):
            return result  # "cutoff" or "failure"
        distancia = sum(
            cidades[result[i]][result[i + 1]] for i in range(len(result) - 1)
        )
        return result, distancia

    elif "Greedy" in algoritmo or "Sôfrega" in algoritmo:
        cost, path = greedyBest_FirstSearch(cidades, origem, destino, linha_reta)
        if path is None:
            return None
        return path, cost

    else:  # A*
        result = a_star_search(cidades, origem, destino, linha_reta)
        if result is None:
            return None
        cost, path = result
        return path, cost


# ── Tab 3: Trip history ───────────────────────────────────────────────────────

def render_tab_historico():
    if not st.session_state.autenticado:
        st.warning("Faz login na barra lateral para ver o histórico.")
        return

    st.header("Histórico de Viagens")

    viagens = [
        v for v in st.session_state.historico
        if v["matricula"] == st.session_state.matricula
    ]

    if not viagens:
        st.info("Ainda não há viagens registadas para esta matrícula.")
        return

    df = pd.DataFrame(viagens)[
        ["data_hora", "algoritmo", "origem", "destino", "distancia", "caminho"]
    ]
    df.columns = ["Data/Hora", "Algoritmo", "Origem", "Destino", "Distância (km)", "Caminho"]
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.download_button(
        "Exportar CSV",
        df.to_csv(index=False).encode("utf-8"),
        file_name=f"historico_{st.session_state.matricula}.csv",
        mime="text/csv",
    )


# ── Tab 4: Tourist attractions ────────────────────────────────────────────────

def render_tab_atracoes():
    if not st.session_state.autenticado:
        st.warning("Faz login na barra lateral para ver as atrações turísticas.")
        return

    st.header("Atrações Turísticas")

    if not st.session_state.ultimo_resultado:
        st.info("Calcula uma rota primeiro para ver as atrações das cidades no percurso.")
        return

    caminho = st.session_state.ultimo_resultado["caminho"]
    st.write(f"Atrações para o percurso: **{' → '.join(caminho)}**")
    st.divider()

    llm = LocalLLM()
    for cidade in caminho:
        with st.expander(f"📍 {cidade}", expanded=True):
            if cidade in st.session_state.llm_cache:
                resultado = st.session_state.llm_cache[cidade]
                st.markdown(resultado["attractions"])
                st.caption("Resposta em cache")
            else:
                with st.spinner(f"A consultar LLM para {cidade}..."):
                    resultado = llm.get_attractions(cidade)
                st.session_state.llm_cache[cidade] = resultado
                st.markdown(resultado["attractions"])
                st.caption(f"Tempo de resposta: {resultado['time']:.2f}s")


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    st.set_page_config(
        page_title="Sistema de Navegação Portugal",
        page_icon="🗺️",
        layout="wide",
    )

    init_session_state()
    render_sidebar_login()

    tab1, tab2, tab3, tab4 = st.tabs([
        "🗺️ Mapa de Cidades",
        "🔍 Planear Rota",
        "📋 Histórico",
        "🏛️ Atrações Turísticas",
    ])

    with tab1:
        render_tab_mapa()
    with tab2:
        render_tab_rota()
    with tab3:
        render_tab_historico()
    with tab4:
        render_tab_atracoes()


if __name__ == "__main__":
    main()

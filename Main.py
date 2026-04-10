import os
from datetime import datetime
os.system('cls' if os.name == 'nt' else 'clear')
from rede import linha_reta, origem_faro, cidades
from ocr_module import LicensePlateOCR
historico_viagens = []
from search_algorithms.uniformCostSearch import uniform_cost_search
from search_algorithms.depthLimitedSearch import depth_limited_search
from search_algorithms.greedyBestFirstSearch import greedyBest_FirstSearch
from search_algorithms.A import a_star_search
from local_llm.LocalLLM import LocalLLM
from spinner import Spinner

def limpar_ecra():
    os.system('cls' if os.name == 'nt' else 'clear')

def registar_viagem(matricula, algoritmo, origem, destino, caminho, distancia):
    """Regista uma viagem no histórico, associada à matrícula."""
    historico_viagens.append({
        'matricula': matricula,
        'algoritmo': algoritmo,
        'origem': origem,
        'destino': destino,
        'caminho': caminho,
        'distancia': distancia,
        'data_hora': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })

def mostrar_historico(matricula):
    """Mostra o histórico de viagens da matrícula atual."""
    print("\n" + "="*60)
    print(f"HISTÓRICO DE VIAGENS — {matricula}")
    print("="*60)
    
    viagens = [v for v in historico_viagens if v['matricula'] == matricula]
    
    if not viagens:
        print("\n  Nenhuma viagem registada ainda.")
    else:
        for i, v in enumerate(viagens, 1):
            print(f"\n  Viagem {i} [{v['data_hora']}]")
            print(f"    Algoritmo: {v['algoritmo']}")
            print(f"    Percurso:  {v['origem']} → {v['destino']}")
            print(f"    Caminho:   {' → '.join(v['caminho'])}")
            print(f"    Distância: {v['distancia']} km")
    
    print("\n" + "="*60)

def mostrar_atracoes_llm(llm, cidades_caminho):
    """Mostra as 3 principais atrações das cidades usando LLM local."""
    print("\n" + "="*60)
    print("ATRAÇÕES TURÍSTICAS (via LLM Local)")
    print("="*60)
    
    for cidade in cidades_caminho:
        print(f"\n{cidade}:")
        with Spinner(f"A pesquisar atrações de {cidade}"):
            resultado = llm.get_attractions(cidade)
        print(resultado['attractions'])
        print(f"   (Tempo de resposta: {resultado['time']:.2f}s)")
    
    print("="*60)

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
    llm = LocalLLM()
    
    while True:
        limpar_ecra()
        print(f"--- BEM-VINDO: {matricula} ---")
        print(f"Percurso: {origem}  →  {destino}\n")
        print("1. Procurar Caminho (Custo Uniforme)")
        print("2. Procurar Caminho (Profundidade Limitada)")
        print("3. Procurar Caminho (Sôfrega)")
        print("4. Procurar Caminho (A*)")
        print("5. Ver Histórico de Viagens")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "0":
            print("A sair...")
            break
        elif opcao == "5":
            mostrar_historico(matricula)
            input("\nPressione Enter para continuar...")
        elif opcao in ("1", "2", "3", "4"):
            if opcao == "1":
                custo, caminho = uniform_cost_search(cidades, origem, destino)
                print(f"\n[Uniform Cost Search]")
                print(f"Custo: {custo} km")
                print(f"Caminho: {' → '.join(caminho)}")
                
                registar_viagem(matricula, "Custo Uniforme", origem, destino, caminho, custo)
                
                # LLM: Atrações turísticas
                mostrar_atracoes_llm(llm, caminho)
                
            elif opcao == "2":
                limite = int(input("Defina o limite de profundidade: "))
                resultado = depth_limited_search(origem, destino, cidades, limite)
                
                if resultado in ("cutoff", "failure"):
                    print(f"\n[Depth Limited Search] Resultado: {resultado}")
                else:
                    print(f"\n[Depth Limited Search]")
                    print(f"Caminho encontrado: {' → '.join(resultado)}")
                    
                    # Calcular distância
                    distancia_total = 0
                    for i in range(len(resultado) - 1):
                        distancia_total += cidades[resultado[i]][resultado[i + 1]]
                    print(f"Distância total: {distancia_total} km")
                    
                    registar_viagem(matricula, f"Profundidade Limitada (l={limite})", origem, destino, resultado, distancia_total)
                    
                    # LLM: Atrações turísticas
                    mostrar_atracoes_llm(llm, resultado)
                
            elif opcao == "3":
                def heuristic(n, goal):
                    return linha_reta(n, goal)
                custo, caminho = greedyBest_FirstSearch(cidades, origem, destino, heuristic)
                print(f"\n[Greedy Best-First Search]")
                print(f"Custo: {custo} km")
                print(f"Caminho: {' → '.join(caminho)}")
                
                registar_viagem(matricula, "Sôfrega (Greedy)", origem, destino, caminho, custo)
                
                # LLM: Atrações turísticas
                mostrar_atracoes_llm(llm, caminho)
                
            elif opcao == "4":
                def heuristic(n, goal):
                    return linha_reta(n, goal)
                custo, caminho = a_star_search(cidades, origem, destino, heuristic)
                print(f"\n[A* Search]")
                print(f"Custo: {custo} km")
                print(f"Caminho: {' → '.join(caminho)}")
                
                registar_viagem(matricula, "A*", origem, destino, caminho, custo)
                
                # LLM: Atrações turísticas
                mostrar_atracoes_llm(llm, caminho)

            input("\nPressione Enter para continuar...")
        else:
            input("Opção inválida. Pressione Enter para tentar de novo...")

def login():
    from ocr_module import GPU_DISPONIVEL
    limpar_ecra()
    print("--- LOGIN DO SISTEMA (OCR) ---\n")

    if GPU_DISPONIVEL:
        escolha = input("GPU detectada. Usar GPU? (s/n): ").strip().lower()
        use_gpu = escolha != "n"
    else:
        print("GPU não detectada. A usar CPU.")
        use_gpu = False

    caminho_imagem = input("\nCaminho para a imagem da matrícula: ").strip()

    if not os.path.isfile(caminho_imagem):
        print(f"Erro: ficheiro não encontrado — {caminho_imagem}")
        return

    print()
    with Spinner(f"A processar imagem com OCR ({'GPU' if use_gpu else 'CPU'})"):
        ocr = LicensePlateOCR(use_gpu=use_gpu)
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

if __name__ == "__main__":
    login()

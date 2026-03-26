import os

os.system('cls' if os.name == 'nt' else 'clear')



from rede import linha_reta, origem_faro, cidades
# Vamos precisar de importar a função de OCR que vais criar
# from ocr_module import extrair_matricula 

def limpar_ecra():
    os.system('cls' if os.name == 'nt' else 'clear')

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

if __name__ == "__main__":
    login()




# Testar o método de Haversine
distancia_teste = linha_reta('Viseu', 'Faro')
print(f"Linha reta Viseu-Faro: {distancia_teste} km")

# Testar a tabela fixa para Faro (Tabela 2)
distancia_faro = origem_faro['Viseu']
print(f"Tabela fixa Viseu-Faro: {distancia_faro} km")

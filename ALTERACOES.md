# 📋 Alterações realizadas — 10/04/2026

Resumo das alterações feitas ao projeto para cumprir todos os requisitos do enunciado.

---

## 1. Heurística corrigida — `rede.py`

**Problema:** A função `linha_reta()` usava **sempre** a fórmula de Haversine (cálculo genérico), ignorando a **Tabela 2 do enunciado** (distâncias em linha reta até Faro).

**Solução:** A função foi dividida em duas:

- `_haversine(origem, destino)` → cálculo genérico (privada, fallback)
- `linha_reta(origem, destino)` → função principal com lógica:
  - Se **destino = Faro** → usa a tabela `origem_faro` (dados do enunciado)
  - Se **origem = Faro** → usa a mesma tabela (distância em linha reta é simétrica)
  - **Caso contrário** → calcula via Haversine

```python
# Exemplo: destino é Faro
linha_reta('Braga', 'Faro')  # → 454 (tabela do enunciado)

# Exemplo: destino NÃO é Faro
linha_reta('Porto', 'Lisboa')  # → Haversine (~274 km)
```

---

## 2. Histórico de Viagens — `Main.py`

**Problema:** A variável `historico_viagens` existia mas nunca era utilizada. O enunciado diz *"Cada caminho deve ser associado a uma matrícula"*.

**Solução:** Implementadas 3 coisas novas:

### `registar_viagem()`
Guarda cada pesquisa com:
- Matrícula (associada via OCR)
- Algoritmo utilizado
- Origem e destino
- Caminho encontrado
- Distância total
- Data/hora

### `mostrar_historico()`
Mostra todas as viagens da matrícula atual num formato legível.

### Menu opção 5
O menu agora tem mais uma opção:
```
1. Procurar Caminho (Custo Uniforme)
2. Procurar Caminho (Profundidade Limitada)
3. Procurar Caminho (Sôfrega)
4. Procurar Caminho (A*)
5. Ver Histórico de Viagens    ← NOVO
0. Sair
```

Cada algoritmo regista automaticamente o resultado após execução com sucesso.

---

## 3. `__init__.py` adicionados

Criados ficheiros `__init__.py` nos dois packages para boa prática Python:
- `search_algorithms/__init__.py`
- `local_llm/__init__.py`

> Nota: Estes ficheiros ficam na **raiz** de cada diretório (ao lado dos outros `.py`), não dentro de nenhuma classe.

---

## 4. Código morto removido — `Main.py`

Removidas as linhas 163-165 que estavam **fora** do `if __name__ == "__main__"`:

```python
# REMOVIDO (era código de teste que crashava ao sair):
distancia_faro = origem_faro['Viseu']
print(f"Tabela fixa Viseu-Faro: {distancia_faro} km")
```

---

## 5. Relatório completado — `relatorio.md`

Todas as secções que estavam vazias (só com `% comentários`) foram preenchidas:

| Capítulo | Secções preenchidas |
|---|---|
| **1. Introdução** | Contextualização, Objetivos (5 pontos), Estrutura do relatório |
| **2. Fundamentação Teórica** | Custo Uniforme, Profundidade Limitada, Greedy, A* (propriedades, complexidade, vantagens/desvantagens), OCR (PaddleOCR), LLM (Llama 3.2, Ollama) |
| **3. Modelação** | Grafo (G=(V,E,w)), tabela distâncias, heurística híbrida (tabela+Haversine), admissibilidade, fórmula Haversine, padrões matrículas |
| **4. Implementação** | Diagrama arquitetura (TikZ), módulo rede, 4 algoritmos com código, interface principal |
| **5. Testes** | 3 cenários (Braga→Faro, Porto→Évora, Bragança→Faro) com tabelas |
| **6. Conclusões** | Análise desempenho, desafios, limitações, melhorias futuras |

---

## ⚠️ O que FALTA fazer

1. **Preencher as tabelas de testes** (Cap. 5 do relatório) — correr o programa nos 3 cenários e meter os caminhos/distâncias reais

2. **Números de aluno na capa** — linhas 173-176 do relatório ainda têm `26...`, `1...`, `27...`

3. **Frontend** — fica para o colega responsável

---

## Estrutura final do projeto

```
AI/
├── Main.py                          # Interface principal + histórico
├── rede.py                          # Grafo + heurística (tabela Faro + Haversine)
├── ocr_module.py                    # OCR com PaddleOCR
├── spinner.py                       # Indicador de progresso
├── requirements.txt                 # Dependências
├── relatorio.md                     # Relatório LaTeX completo
├── seat.png                         # Imagem teste OCR
├── search_algorithms/
│   ├── __init__.py                  # NOVO
│   ├── uniformCostSearch.py         # Custo Uniforme
│   ├── depthLimitedSearch.py        # Profundidade Limitada
│   ├── greedyBestFirstSearch.py     # Sôfrega
│   └── A.py                        # A*
└── local_llm/
    ├── __init__.py                  # NOVO
    └── LocalLLM.py                  # LLM local (Ollama)
```

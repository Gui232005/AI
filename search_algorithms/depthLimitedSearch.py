'''
    O Depth_limited Search é um algoritmo que pesquisa em profundidade, mas com um limite de profundidade definido.  
'''

# Esta função expande um nó, retornando seus vizinhos. No nosso caso, os vizinhos são as cidades conectadas ao nó atual no grafo.
def expand(node, graph):
    return list(graph[node].keys())

# Esta verifica se o nó atual é o objetivo. Se for, retorna True, caso contrário, retorna False.
def goal_test(node, goal):
    return node == goal

# Aqui é onde o algoritmo está implementado, quando o limite for atingido ele para nao interessa se chegou ou nao ao objetivo
def depth_limited_search(node, goal, graph, limit):
    if goal_test(node, goal):
        return [node]
    elif limit == 0:
        return "cutoff"
    else:
        cutoff_occurred = False
        for child in expand(node, graph):
            result = depth_limited_search(child, goal, graph, limit - 1) # Conforme a pesquisa é feita em cada nível, o limite é decrementado
            if result == "cutoff":
                cutoff_occurred = True
            elif result != "failure":
                return [node] + result  # Constrói o caminho
        return "cutoff" if cutoff_occurred else "failure"
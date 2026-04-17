'''
    O Depth_limited Search é um algoritmo que pesquisa em profundidade, mas com um limite de profundidade definido.
'''

# Aqui é onde o algoritmo está implementado, quando o limite for atingido ele para nao interessa se chegou ou nao ao objetivo
def depth_limited_search(node, goal, graph, limit=18, visited=None):
    # Limite defenido em 18 porque é o número máximo de cidades, ou seja, o número máximo de nós que podem ser visitados
    if ((limit > 18) or (limit <= 0)):
        limit = 18
    # O parâmetro visited é para que o algoritmo não passe no mesmo local mais do que uma vez
    if visited is None:
        visited = set()
    if node == goal:
        return [node]
    elif limit == 0:
        return "cutoff"
    elif node in visited:
        return "failure"
    else:
        visited.add(node)
        cutoff_occurred = False
        for child in graph[node].keys():
            result = depth_limited_search(child, goal, graph, limit - 1, visited)
            print("Interação: ", node, " -> ", child, " | km: ", graph[node][child], " | Resultado: ", result)
            if result == "cutoff":
                cutoff_occurred = True
            elif result != "failure":
                return [node] + result  # Constrói o caminho
        return "cutoff" if cutoff_occurred else "failure"
import heapq

'''
    Este algoritmo de pesquisa é cego, não tem qualquer infomação adicional, e faz a escolha do caminho tendo em conta o custo total acumulado para chegar a um nó, 
garantindo que o caminho mais barato é sempre expandido primeiro. 
    Ele é especialmente útil quando os custos entre os nós variam, como no caso de distâncias entre cidades.
'''

def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start, [start])]  # Aqui o custo é a prioridade, seguido do nó atual e do caminho percorrido
    visited = {}  # Guarda o custo mínimo para cada nó

    while priority_queue:
        current_cost, current_node, path = heapq.heappop(priority_queue)

        if current_node == goal:
            return current_cost, path  # Retorna o custo total e o caminho

        if current_node in visited and visited[current_node] <= current_cost:
            continue  # Ignora se já encontrámos um caminho mais barato

        visited[current_node] = current_cost

        for neighbor, cost in graph[current_node].items():  # Usa .items() para fazer um loop sobre os vizinhos e seus custos
            total_cost = current_cost + cost
            new_path = path + [neighbor]
            print("Interação: ", current_node, " -> ", neighbor, " | km: ", cost, " | Custo total: ", total_cost)

            if neighbor not in visited or total_cost < visited.get(neighbor, float('inf')):
                heapq.heappush(priority_queue, (total_cost, neighbor, new_path))

    return None  # Retorna None se não houver caminho entre start e goal

import heapq

'''
    O A* é um algoritmo que junta outros dois algoritmos, o Uniform Cost Search e o Greedy Best-First Search. 
    O A* expande os nós com o menor valor do nó onde está, garantindo que o caminho mais barato seja sempre expandido primeiro, 
enquanto também leva em consideração a proximidade do objetivo.
'''

def a_star_search(graph, start, goal, heuristic):
    priority_queue = []
    initial_h = heuristic(start, goal)
    heapq.heappush(priority_queue, (0 + initial_h, 0, start, [start]))  # (f(n), g(n), node, path)
    visited = {}  # Guarda o custo mínimo para cada nó

    while priority_queue:
        f_cost, g_cost, current_node, path = heapq.heappop(priority_queue)

        if current_node == goal:
            return g_cost, path  # Retorna o custo total e o caminho

        if current_node in visited and visited[current_node] <= g_cost:
            continue  # Ignora se já encontrámos um caminho mais barato

        visited[current_node] = g_cost

        for neighbor, cost in graph[current_node].items():
            total_g_cost = g_cost + cost
            neighbor_h = heuristic(neighbor, goal)
            total_f_cost = total_g_cost + neighbor_h
            new_path = path + [neighbor]

            if neighbor not in visited or total_g_cost < visited.get(neighbor, float('inf')):
                heapq.heappush(priority_queue, (total_f_cost, total_g_cost, neighbor, new_path))

    return None  # Retorna None se não houver caminho
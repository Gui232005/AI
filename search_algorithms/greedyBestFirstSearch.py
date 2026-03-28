import heapq

'''
    O Greedy Best-First Search é um algoritmo de procura que estima o custo restante até o objetivo.
    Ele sempre expande o nó que parece estar mais próximo do objetivo sem considerar o custo acumulado para chegar a esse nó.
'''

def greedyBest_FirstSearch(graph, start, goal, heuristic):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic(start, goal), start))

    visited = set()
    parent = {start: None}

    while priority_queue:
        _, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            # Reconstruir o caminho
            path = []
            node = current_node
            while node is not None:
                path.append(node)
                node = parent[node]
            path = path[::-1]  # Inverte o caminho, para que vá do início ao objetivo

            # Calcular o custo total do caminho
            total_cost = 0
            for i in range(len(path) - 1):
                total_cost += graph[path[i]][path[i + 1]]

            return total_cost, path  # Devolve (custo, caminho)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                parent[neighbor] = current_node
                heapq.heappush(priority_queue, (heuristic(neighbor, goal), neighbor))

    return None, None  # Se não houver caminho
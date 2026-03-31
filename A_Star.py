import heapq

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))  # (f_cost, node)
    came_from = {}
    g_cost = {start: 0}

    while open_list:
        current_cost, current = heapq.heappop(open_list)

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # reverse path

        for neighbor, edge_cost in graph.get(current, []):
            tentative_g = g_cost[current] + edge_cost
            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                came_from[neighbor] = current
                g_cost[neighbor] = tentative_g
                f = tentative_g + heuristic[neighbor]
                heapq.heappush(open_list, (f, neighbor))

    return None

# Example graph and heuristic
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 1), ('E', 2)],
    'C': [('F', 5), ('G', 2)],
    'D': [],
    'E': [('H', 1)],
    'F': [],
    'G': [('H', 3)],
    'H': []
}

heuristic = {
    'A': 7, 'B': 6, 'C': 4,
    'D': 5, 'E': 2, 'F': 3,
    'G': 2, 'H': 0
}

start_node = 'A'
goal_node = 'H'

path = a_star(graph, start_node, goal_node, heuristic)

if path:
    print(f"Shortest path: {' -> '.join(path)}")
else:
    print("No path found.")
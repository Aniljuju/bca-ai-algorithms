def ida_star(graph, start, goal, heuristic):
    def dfs(current, g_cost, threshold, path):
        # Calculate f-cost: g(n) + h(n)
        f_cost = g_cost + heuristic[current]
        if f_cost > threshold:
            return float('inf')  # Prune if f-cost exceeds threshold

        path.append(current)  # Add current node to path

        if current == goal:
            return path  # Goal found, return the path

        min_exceeded = float('inf')  # Track smallest f-cost exceeding threshold
        for neighbor, cost in graph.get(current, []):
            if neighbor not in path:  # Avoid cycles
                new_g_cost = g_cost + cost
                result = dfs(neighbor, new_g_cost, threshold, path)
                if isinstance(result, list):
                    return result  # Propagate path if goal is found
                if result < min_exceeded:
                    min_exceeded = result  # Update minimum exceeded threshold

        path.pop()  # Backtrack by removing current node
        return min_exceeded

    # Start with initial threshold based on heuristic of start node
    threshold = heuristic[start]
    while True:
        path = []  # Initialize path for each iteration
        result = dfs(start, 0, threshold, path)
        if isinstance(result, list):
            return result  # Return path if goal is found
        if result == float('inf'):
            return None  # No path exists
        threshold = result  # Increase threshold for next iteration

graph = {
    'A': [('B', 1), ('C', 2)],
    'B': [('D', 3), ('E', 2)],
    'C': [('D', 1)],
    'D': [],
    'E': [('D', 1)]
}

heuristic = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 0,
    'E': 1
}

start_node = 'A'
goal_node = 'D'

path = ida_star(graph, start_node, goal_node, heuristic)
if path:
    print(f"Path found: {' -> '.join(path)}")
else:
    print("No path found.")
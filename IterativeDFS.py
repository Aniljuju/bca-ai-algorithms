def dfs_iterative(graph, start_node):
    visited = set()
    stack = [start_node]

    print("DFS Iterative Traversal:", end=" ")

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.add(current)
            print(current, end=" ")

            # Push neighbors in their original order
            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)

    print()


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

dfs_iterative(graph, 'A')
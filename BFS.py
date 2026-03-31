from collections import deque

def bfs(graph, start_node):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start_node])  # Initialize the queue with the start node
    visited.add(start_node)

    print("BFS Traversal:", end=" ")

    while queue:
        current = queue.popleft()  # Dequeue a node
        print(current, end=" ")    # Process the node (e.g., print it)

        # Enqueue unvisited neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

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

start_node = 'A'
bfs(graph, start_node)
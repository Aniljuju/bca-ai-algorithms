import heapq

def best_first_search(graph, start, target, heuristic):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))
    visited = set()

    print("Best-First Search Traversal:", end=" ")

    while priority_queue:
        h_value, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)
        print(current, end=" ")

        if current == target:
            print(f"\nTarget '{target}' found!")
            return

        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))

    print("\nTarget not found.")


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 6,
    'G': 5,
    'H': 1
}

start_node = 'A'
target_node = 'H'

best_first_search(graph, start_node, target_node, heuristic)
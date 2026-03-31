def iddfs(graph, start, target):

    def dls(current, target, depth, path):
        if depth == 0 and current == target:
            return path + [current]
        if depth > 0:
            for neighbor in graph.get(current, []):
                result = dls(neighbor, target, depth - 1, path + [current])
                if result:
                    return result
        return None

    depth = 0
    while True:
        print(f"Searching at depth {depth}...")
        result = dls(start, target, depth, [])
        if result:
            return result
        depth += 1


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

start_node = 'A'
target_node = 'H'
path = iddfs(graph, start_node, target_node)

print(f"Path to target '{target_node}': {' -> '.join(path)}")
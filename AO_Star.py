import heapq

# Define Node class
class Node:
    def __init__(self, name, node_type, heuristic):
        self.name = name
        self.node_type = node_type  # 'AND', 'OR', 'LEAF'
        self.heuristic = heuristic
        self.children = []          # List of tuples (child_node, edge_cost)
        self.cost = float('inf')
        self.solved = False
        self.parents = []

    def __lt__(self, other):
        return self.cost < other.cost

# AO* algorithm implementation
def ao_star(root, all_nodes):
    open_list = []

    # Initialize unsolved nodes with heuristic costs
    for node in all_nodes:
        if not node.solved:
            node.cost = node.heuristic
            heapq.heappush(open_list, (node.cost, node))

    while open_list:
        current_cost, current = heapq.heappop(open_list)

        if current.solved:
            continue

        old_cost = current.cost

        if current.node_type == 'OR':
            # Solve OR node: choose child with minimal total cost
            min_child, min_edge_cost = min(
                current.children, key=lambda x: x[0].cost + x[1]
            )
            current.cost = min_child.cost + min_edge_cost
            current.solved = min_child.solved

        elif current.node_type == 'AND':
            # Solve AND node: sum costs of all children
            total_cost = sum(child.cost + edge_cost for child, edge_cost in current.children)
            all_solved = all(child.solved for child, _ in current.children)
            current.cost = total_cost
            current.solved = all_solved

        # If cost changed or node is solved, propagate update to parents
        if current.cost != old_cost or current.solved:
            propagate(current, open_list)

        if current.solved:
            print(f"Node {current.name} solved with cost {current.cost}")
            if current == root:
                break
        else:
            # Reinsert current node to open_list if not yet solved
            heapq.heappush(open_list, (current.cost, current))

    return root.cost if root.solved else None

# Propagate updates to parent nodes
def propagate(node, open_list):
    for parent in node.parents:
        heapq.heappush(open_list, (parent.cost, parent))

# -------------------------------
# Example graph setup
# -------------------------------
A = Node('A', 'OR', 7)
B = Node('B', 'AND', 6)
C = Node('C', 'OR', 5)
D = Node('D', 'LEAF', 3)
E = Node('E', 'LEAF', 2)

# Define children and edge costs
A.children = [(B, 1), (C, 2)]
B.children = [(D, 3), (E, 4)]
C.children = [(E, 1)]

# Set leaf nodes as solved
D.solved = True
E.solved = True

D.cost = 0
E.cost = 0

# Define parent links
B.parents = [A]
C.parents = [A]
D.parents = [B]
E.parents = [B, C]

# List of all nodes for AO*
all_nodes = [A, B, C, D, E]

# Solve the root node
optimal_cost = ao_star(A, all_nodes)

print(f"Optimal cost to solve root node: {optimal_cost}")
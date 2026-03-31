from collections import deque

def water_jug(m, n, d):
    visited = set()
    queue = deque()

    queue.append((0, 0))  # start from empty jugs

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        print(x, y)  # show states
        visited.add((x, y))

        # check solution
        if x == d or y == d:
            print("Solution found")
            return

        # possible next states
        next_states = [
            (m, y),  # fill jug1
            (x, n),  # fill jug2
            (0, y),  # empty jug1
            (x, 0),  # empty jug2

            # pour jug1 -> jug2
            (x - min(x, n - y), y + min(x, n - y)),

            # pour jug2 -> jug1
            (x + min(y, m - x), y - min(y, m - x))
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

    print("No solution")


# Example
water_jug(4, 3, 2)
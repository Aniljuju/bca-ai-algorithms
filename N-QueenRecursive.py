def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_n_queens_backtracking(N, board=None, row=0, solutions=None):
    if board is None:
        board = []
    if solutions is None:
        solutions = []

    if row == N:
        solutions.append(board.copy())
        if len(solutions) <= 2:  # Only print first two solutions
            print(f"Solution {len(solutions)}:", board)
        return solutions

    for col in range(N):
        if is_safe(board, row, col):
            board.append(col)
            solve_n_queens_backtracking(N, board, row + 1, solutions)
            board.pop()

    return solutions


# Run for N = 5
solutions = solve_n_queens_backtracking(5)
print("Total solutions:", len(solutions))
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(i - row) == abs(board[i] - col):
            return False
    return True

def solve_n_queens_iterative(N):
    stack = []
    board = [-1] * N
    row = 0
    
    while row < N:
        placed = False
        start_col = board[row] + 1 if board[row] != -1 else 0
        
        for col in range(start_col, N):
            if is_safe(board, row, col):
                board[row] = col
                stack.append((row, col))
                placed = True
                break;
        
        if not placed:
            if not stack:
                print("No solution")
                return
            board[row] = -1
            row, _ = stack.pop()
        else:
            row += 1
    
    print("Solution:", board)
solve_n_queens_iterative(5)
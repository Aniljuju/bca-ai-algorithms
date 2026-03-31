import math

def evaluate(board):
    # Check for wins or losses
    if check_win(board, "X"):
        return 10
    elif check_win(board, "O"):
        return -10
    elif " " not in board:
        return 0  # Draw
    else:
        # Heuristic: Prefer the center position
        if board[4] == "X":
            return 1
        else:
            return 0


def check_win(board, player):
    # Check rows, columns, and diagonals
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False


def min_max(board, depth, is_maximizer):
    score = evaluate(board)

    if score == 10 or score == -10 or " " not in board:
        return score

    if is_maximizer:
        best = -math.inf
        for move in possible_moves(board):
            make_move(board, move, "X")
            best = max(best, min_max(board, depth+1, False))
            undo_move(board, move)
        return best    #moved outside loop

    else:
        best = math.inf
        for move in possible_moves(board):
            make_move(board, move, "O")
            best = min(best, min_max(board, depth+1, True))
            undo_move(board, move)
        return best    #moved outside loop


def possible_moves(board):
    # Prioritize the center position (4) if available
    if board[4] == " ":
        return [4] + [i for i in range(9) if board[i] == " " and i != 4]
    else:
        return [i for i in range(9) if board[i] == " "]


def make_move(board, move, player):
    board[move] = player


def undo_move(board, move):
    board[move] = " "


board = [" "] * 9  # Empty Tic-Tac-Toe board
best_move = None
best_val = -math.inf

for move in possible_moves(board):
    make_move(board, move, "X")
    move_val = min_max(board, 0, False)
    undo_move(board, move)

    if move_val > best_val:
        best_val = move_val
        best_move = move

print("Best move for Maximizer (X): Position", best_move)
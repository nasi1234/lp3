def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(board, row, n, fixed_row, fixed_col):
    if row >= n:
        return True

    # Skip the fixed queen’s row
    if row == fixed_row:
        return solve_nqueens(board, row + 1, n, fixed_row, fixed_col)
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_nqueens(board, row + 1, n, fixed_row, fixed_col):
                return True

            board[row][col] = 0
    return False

def n_queens_with_first_queen(n, first_row, first_col):
    board = [[0] * n for _ in range(n)]
    board[first_row][first_col] = 1

    if solve_nqueens(board, 0, n, first_row, first_col):
        print("Solution found:")
        print_board(board)
    else:
        print("No solution exists for this configuration.")

# Input
n = int(input("Enter the size of the chessboard (n): "))
first_row = int(input("Enter the row index of the first queen (0 to n-1): "))
first_col = int(input("Enter the column index of the first queen (0 to n-1): "))

if 0 <= first_row < n and 0 <= first_col < n:
    n_queens_with_first_queen(n, first_row, first_col)
else:
    print("Invalid position for the first queen.")

def is_safe(board, row, col, n):
    # Check if there is a Queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
        
    #  # Check lower-left diagonal
    # for i, j in zip(range(row, n), range(col, -1, -1)):
    #     if board[i][j] == 1:
    #         return False

    # # Check lower-right diagonal
    # for i, j in zip(range(row, n), range(col, n)):
    #     if board[i][j] == 1:
    #         return False

    return True

def solve_n_queens(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_n_queens(board, row + 1, n):
                return True

            board[row][col] = 0

    return False

def print_board(board):
    for row in board:
        print(" ".join(["Q" if cell == 1 else "." for cell in row]))


def place_queens_with_valid_first_queen(n):
    if n < 1:
        return None

    board = [[0 for _ in range(n)] for _ in range(n)]
    
    # Place the first Queen in the first row, leftmost column
    first_queen_row, first_queen_col = 0, 0
    board[first_queen_row][first_queen_col] = 1
    
    # Place the remaining Queens using backtracking
    if solve_n_queens(board, 1, n):  # Start from the second row
        print("Solution found:")
        print_board(board)
    else:
        print("No solution found for the given configuration.")

if __name__ == "__main__":
    n = 8  # Change this to the desired value of 'n'
    
    place_queens_with_valid_first_queen(n)


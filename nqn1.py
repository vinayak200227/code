N = 4

def printsol(board):
	for i in range(N):
		for j in range(N):
			print(board[i][j], end=' ')
		print()


def isSafe(board, row, col):
	for i in range(col):
		if board[row][i] == 'V':
			return False

	for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
		if board[i][j] == 'V':
			return False

	for i, j in zip(range(row, N, 1), range(col, -1, -1)):
		if board[i][j] == 'V':
			return False
	return True


def NQ(board, col, solutions):
	if col >= N:
		solutions.append([row[:] for row in board])
		return

	for i in range(N):
		if isSafe(board, i, col):
			board[i][col] = 'V'
			NQ(board, col+1, solutions)
			board[i][col] = 0


def main():
	board = [[0 for i in range(N)] for j in range(N)]
	solutions = []
	NQ(board, 0, solutions)
    
	print(f"Number of solutions {len(solutions)}")
	if solutions:
		for board in solutions:
			printsol(board)
			print()
	else:
		print("No solutions found.")


main()

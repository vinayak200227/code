class NQueenProblem:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.solutions = []

    def solve(self):
        self._place_queen(0)
        return self.solutions

    def _is_safe(self, row, col):
        # Check if it is safe to place a queen at the given position
        # Check row and column
        for i in range(self.n):
            if self.board[row][i] == 1 or self.board[i][col] == 1:
                return False

        # Check upper diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check lower diagonal
        for i, j in zip(range(row, self.n, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def _place_queen(self, col):
        if col == self.n:
            # All queens have been placed, add the solution
            solution = []
            for row in self.board:
                solution.append(''.join(['Q' if x == 1 else '.' for x in row]))
            self.solutions.append(solution)
            return True

        for row in range(self.n):
            if self._is_safe(row, col):
                self.board[row][col] = 1

                # Recursively place queens in the next column
                self._place_queen(col + 1)

                # Backtrack
                self.board[row][col] = 0

    def print_solutions(self):
        for solution in self.solutions:
            for row in solution:
                print(row)
            print()


# Usage
n = int(input("Enter the size of the chessboard (N): "))
queen_problem = NQueenProblem(n)
solutions = queen_problem.solve()
print("Total solutions:", len(solutions))
queen_problem.print_solutions()


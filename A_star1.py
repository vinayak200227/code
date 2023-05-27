import heapq


N = 3

# Structure to represent a node in the puzzle
class Node:
    def __init__(self, mat, x, y, g, p=None):
        self.p = p       # Parent node
        self.mat = mat   # Puzzle matrix
        self.x = x       # Blank tile coordinates
        self.y = y
        self.h = 0       # Heuristic value (Manhattan distance)
        self.g = g       # Cost to reach this node from the initial state
        self.f = 0       # Evaluation function value (g + h)

    def __lt__(self, other):
        # print("less than operator overloaded")
        return self.f < other.f


# Print the puzzle matrix
def pr(mat):
    for i in range(N):
        for j in range(N):
            print(mat[i][j], end="  ")
        print()


# Create a new node with updated puzzle matrix and coordinates
def newNode(mat, x, y, nx, ny, g, p):
    node = Node(mat, nx, ny, g, p)

    # Copy the puzzle matrix
    node.mat = [row[:] for row in mat]

    # Swap the blank tile with the new coordinates
    node.mat[x][y], node.mat[nx][ny] = node.mat[nx][ny], node.mat[x][y]

    node.h = float("inf")

    return node


# Calculate the number of misplaced tiles between two matrices
def diff(imat, res):
    count = 0
    for i in range(N):
        for j in range(N):
            if imat[i][j] != res[i][j]:
                count += 1
    return count


# Arrays to represent possible movements in the puzzle
r = [1, 0, -1, 0]
c = [0, -1, 0, 1]


# Check if a movement is valid within the puzzle boundaries
def move(x, y):
    return (x >= 0 and x < N and y >= 0 and y < N)


# Traverse and print the solution path
def trv(root):
    if root is None:
        return

    trv(root.p)
    pr(root.mat)
    print()


# A* algorithm to solve the 8 puzzle problem
def solve(imat, x, y, res):
    # Priority queue to store the open list of nodes to be expanded
    pq = []

    # Create the root node
    root = newNode(imat, x, y, x, y, 0, None)
    root.h = diff(imat, res)
    root.f = root.g + root.h

    heapq.heappush(pq, root)

    while pq:
        temp = heapq.heappop(pq)

        # If the current node is the goal state, print the solution
        if temp.h == 0:
            trv(temp)
            print()
            return

        # Generate the successors of the current node
        for i in range(4):
            if move(temp.x + r[i], temp.y + c[i]):
                # Create a new child node
                child = newNode(temp.mat, temp.x, temp.y, (temp.x + r[i]), (temp.y + c[i]), (temp.g + 1), temp)
                child.h = diff(child.mat, res)
                child.f = child.g + child.h

                heapq.heappush(pq, child)


# Initial and goal states of the puzzle
imat = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

res = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

# Initial position of the blank tile in the initial state
x, y = 2, 1

# Solve the puzzle using A* algorithm
solve(imat, x, y, res)

#Implement a solution for a Constraint Satisfaction Problem using Branch and 
Bound and Backtracking for n-queens problem or a graph coloring problem. 

# N-Queens Problem Solution
def is_safe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, N):
    if col >= N:
        return True
    
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1  # Place the queen
            if solve_n_queens(board, col + 1, N):
                return True
            board[i][col] = 0  # Backtrack
    
    return False

def n_queens_branch_and_bound(N):
    board = [[0] * N for _ in range(N)]
    if not solve_n_queens(board, 0, N):
        print("No solution exists")
        return
    print("Solution for", N, "Queens:")
    for row in board:
        print(row)

# Main execution for N-Queens
N = int(input("Enter the number of queens: "))
n_queens_branch_and_bound(N)


# Graph Coloring Problem Solution
def is_safe_graph(graph, color, v, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, v):
    if v == len(graph):
        return True
    
    for c in range(1, m + 1):
        if is_safe_graph(graph, color, v, c):
            color[v] = c
            if graph_coloring_util(graph, m, color, v + 1):
                return True
            color[v] = 0
    
    return False

def graph_coloring(graph, m):
    color = [0] * len(graph)
    
    if not graph_coloring_util(graph, m, color, 0):
        print("Solution does not exist")
        return
    
    print("Solution exists: Following are the assigned colors")
    for v in range(len(graph)):
        print("Vertex", v, " --->  Color", color[v])

# Example graph for Graph Coloring
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
m = 3  # Number of colors

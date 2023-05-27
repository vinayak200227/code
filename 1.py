from collections import deque

# def dfs(graph, start):
#     queue = deque([start])
#     visited = set()

#     while queue:
#         vertex = queue.pop()
#         if vertex not in visited:
#             visited.add(vertex)
#             print(vertex)

#             for n in graph[vertex]:
#                 queue.append(n)

def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    vertex = start
    visited.add(vertex)
    print(vertex)

    for child in graph[vertex]:
        if child not in visited:
            dfs(graph, child, visited)






def bfs(graph, start):
    queue = deque([start])
    visited = set()

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)

            for n in graph[vertex]:
                queue.append(n)



Graph = {
    'A':['B','C'],
    'B':['D','E','A'],
    'C':['F','G','A'],
    'G':['C'],
    'F':['C'],
    'E':['B'],
    'D':['B']
}

print("DFS is ")
dfs(Graph, 'A')

print()

print("BFS is ")
bfs(Graph, 'A')

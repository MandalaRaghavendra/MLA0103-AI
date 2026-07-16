from collections import deque

# BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    print("BFS Traversal:", end=" ")
    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# DFS
def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Input
n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

graph = {}

for i in range(1, n + 1):
    graph[i] = []

print("Enter edges (u v):")
for i in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)   # Remove this line for a directed graph

start = int(input("Enter starting node: "))

# BFS
bfs(graph, start)

# DFS
print("\nDFS Traversal:", end=" ")
visited = set()
dfs(graph, start, visited)

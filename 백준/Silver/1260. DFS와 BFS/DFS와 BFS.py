from collections import deque, defaultdict

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for neighbor in sorted(graph[start]):
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = {i: False for i in graph}
    queue = deque([start])
    visited[start] = True
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for neighbor in sorted(graph[vertex]):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
V = int(data[2])
edges = data[3:]

graph = defaultdict(list)
for i in range(M):
    u = int(edges[2*i])
    v = int(edges[2*i + 1])
    graph[u].append(v)
    graph[v].append(u)

visited_dfs = {i: False for i in range(1, N+1)}
dfs(graph, V, visited_dfs)
print()
bfs(graph, V)
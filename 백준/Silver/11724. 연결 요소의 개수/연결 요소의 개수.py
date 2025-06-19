import sys
sys.setrecursionlimit(10**6)

def dfs(graph, v, visited):
    visited[v] = True

    for select_v in graph[v]:
        if not visited[select_v]:
            dfs(graph, select_v, visited)

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# 그래프 구축
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())

    graph[x].append(y)
    graph[y].append(x)

count = 0

for v in range(1, n+1):
    if not visited[v]:
        dfs(graph, v, visited)
        count += 1

print(count)
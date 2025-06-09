from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for select_v in graph[v]:
        if not visited[select_v]:
            dfs(graph, select_v, visited)

def bfs(graph, start_v, visited):
    queue = deque()
    queue.append(start_v)
    visited[start_v] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for select_v in graph[v]:
            if not visited[select_v]:
                queue.append(select_v)
                visited[select_v] = True

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

# 그래프 구축
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드별 정렬
for i in range(1, N+1):
    graph[i].sort()

visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)
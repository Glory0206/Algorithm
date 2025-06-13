from collections import deque

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))

result = 0
for line in box:
    for tomato in line:
        if tomato == 0:
            print(-1)
            exit()
        result = max(result, tomato)

print(result - 1)
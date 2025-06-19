from collections import deque

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(start_x, start_y, cabbage_positions, visited):
    bfs_q = deque()
    bfs_q.append((start_x, start_y))
    visited.add((start_x, start_y))

    while bfs_q:
        x, y = bfs_q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx, ny) in cabbage_positions and (nx, ny) not in visited:
                visited.add((nx, ny))
                bfs_q.append((nx, ny))


# 테스트 케이스 수
test = int(input())

for _ in range(test):
    m, n, k = map(int, input().split())

    # 배추 위치 저장
    cabbage_positions = set(tuple(map(int, input().split())) for _ in range(k))

    # 방문 좌표 박스, count 횟수 초기화
    visited = set()
    count = 0

    # 한 번의 bfs로 배추 한 묶음 확인
    for position in cabbage_positions:
        #  bfs를 진행하며 방문했던 좌표가 초기의 배추 좌표에 있을 경우 다음 좌표로 넘김
        if position not in visited:
            bfs(position[0], position[1], cabbage_positions, visited)
            count += 1

    print(count)

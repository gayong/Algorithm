from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y, num):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n:
                if low[nx][ny] > num and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

n = int(input())
max_num = 0

low = [list(map(int, input().split())) for _ in range(n)]

for i in low:
    for j in i:
        if j > max_num:
            max_num = j
# print(low)
# print(max_num)

result = []

for i in range(max_num):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if low[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i)
                cnt += 1
    result.append(cnt)

print(max(result))
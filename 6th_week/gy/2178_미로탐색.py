import sys
sys.stdin = open('input.txt')
from collections import deque

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def bfs(x, y):
    global N, M
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y]
            break
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] != 0 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    return visited[x][y]


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]

x, y = 0, 0
print(bfs(x, y))
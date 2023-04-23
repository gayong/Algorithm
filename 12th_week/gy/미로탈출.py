from collections import deque

# 시작 -> 레버 / 레버 -> 도착 두 번 경로 탐색
# 전체를 탐색하며 시작 좌표, 레버 좌표 반환하는 find 함수
# 도달 불가 시 -1을 반환하는 bfs 함수
# 두 번의 경로탐색 후 둘 중 하나라도 -1이면 -1 반환하는 solution 함수

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find(maps):
    n, m = len(maps), len(maps[0])
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = j, i
            if maps[i][j] == 'L':
                lever = j, i
    return start, lever

def bfs(start, maps, goal):
    n, m = len(maps), len(maps[0])
    x, y = start
    visited = [[0]*m for _ in range(n)]
    visited[y][x] = 1
    q = deque([(x, y, 0)])
    while q:
        x, y, dist = q.popleft()
        if maps[y][x] == goal:
            return dist
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == 0 and maps[ny][nx] != 'X':
                visited[ny][nx] = 1
                q.append((nx, ny, dist+1))
    return -1

def solution(maps):
    start, lever = find(maps)
    lever_dist = bfs(start, maps, 'L')
    end_dist = bfs(lever, maps, 'E')
    if lever_dist > -1 and end_dist > -1:
        return lever_dist + end_dist
    else:
        return -1

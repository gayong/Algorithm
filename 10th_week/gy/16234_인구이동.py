import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    q = deque()
    temp = []
    q.append((a, b))
    temp.append((a, b)) # 국경선 공유하는 나라들 좌표 넣음
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                # 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    temp.append((nx, ny))
    return temp

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0

while 1:
    visited = [[0] * (n + 1) for _ in range(n + 1)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)
                # 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
                # flag 1로 바꿔서 인구 이동 시작됐음을 표시
                if len(country) > 1:
                    flag = 1
                    # 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
                    number = sum([graph[x][y] for x, y in country]) // len(country)
                    for x, y in country:
                        graph[x][y] = number # 국경 공유하는 나라들 인구수 갱신
    # 모든 조건 완료됐으면 연합을 해체하고, 모든 국경선을 닫는다.
    if flag == 0:
        break
    result += 1 # while문 한번 돌 때마다 result += 1 (인구이동 몇일?)
print(result)
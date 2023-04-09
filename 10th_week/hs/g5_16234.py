import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
used = True
result = 0

while used:
    used = False
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                group = []
                group_sum = 0
                stack = [(i, j)]
                visited[i][j] = 1

                while stack:
                    x, y = stack.pop()
                    group.append((x, y))
                    group_sum += arr[x][y]

                    for k in range(4):
                        for t in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                                continue
                            diff = abs(arr[nx][ny] - arr[x][y])
                            if L <= diff <= R and not visited[nx][ny]:
                                stack.append((nx, ny))
                                visited[nx][ny] = 1
                                used = True

                length = len(group)
                if length >= 2:
                    avg = group_sum // length
                    for k in range(length):
                        arr[group[k][0]][group[k][1]] = avg
    if used:
        result += 1

print(result)

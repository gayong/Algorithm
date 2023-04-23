from collections import deque

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

def solution(maps):
    height = len(maps)
    width = len(maps[0])
    visited = [[0] * width for _ in range(height)]
    q = deque()
    for i in range(height):
        for j in range(width):
            if maps[i][j] == 'S':
                q.append((j, i, 0, 0))
                visited[i][j] = 1
    
    while q:
        x, y, uselever, cnt = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 > nx or width <= nx or 0 > ny or height <= ny:
                continue
            if maps[ny][nx] != 'X':
                if not uselever:
                    if not visited[ny][nx]:
                        visited[ny][nx] = 1
                        if maps[ny][nx] == 'L':
                            q.append((nx, ny, uselever+1, cnt+1))
                        else:
                            q.append((nx, ny, uselever, cnt+1))
                    continue
                else:
                    if visited[ny][nx] != 2:
                        visited[ny][nx] = 2
                        q.append((nx,ny, uselever, cnt+1))
                        if maps[ny][nx] == 'E':
                            return cnt+1

    return -1

print(solution([list(input()) for _ in range(5)]))
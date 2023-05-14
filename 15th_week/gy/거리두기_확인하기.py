from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(arr):
    start = []
    for i in range(5):
        for j in range(5):
            if arr[i][j] == 'P':
                start.append([i, j])
    for s in start:
        q = deque([s])
        visited = [[0]*5 for i in range(5)]
        distance = [[0]*5 for i in range(5)] # 거리 계산용
        visited[s[0]][s[1]] = 1
        
        while q:
            y, x = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0:
                    if arr[ny][nx] == 'O':
                        q.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1
                        
                    if arr[ny][nx] == 'P' and distance[y][x] <= 1: # P 발견했을때 시작점부터의 거리가 1보다 작거나 같을 경우
                        return 0
                        break
    return 1

def solution(places):
    answer = []
    for i in places:
        answer.append(bfs(i))
    return answer

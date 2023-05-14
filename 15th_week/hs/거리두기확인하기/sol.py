from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(place):
    p_list = []

    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                p_list.append([i, j])

    for p in p_list:
        q = deque([p])
        visited = [[0] * 5 for _ in range(5)]
        distance = [[0] * 5 for _ in range(5)]
        visited[p[0]][p[1]] = 1

        while q:
            y, x = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 > nx or nx >= 5 or 0 > ny or ny >= 5:
                    continue
                if visited[ny][nx] == 0:
                    if place[ny][nx] == 'O':
                        q.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1

                    if place[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1

def solution(places):
    
    answer = []

    for place in places:
        answer.append(bfs(place))

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
      "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

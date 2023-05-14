'''
플로이드-워셜
모든 점끼리 최단거리 구하기 > 모든 점에서 시작해서 s,a,b까지의 거리를 합한 것 중 최솟값 찾기
'''

INF = 9876543210

def solution(n, s, a, b, fares):
    cost_board = [[INF] * (n + 1) for _ in range(n + 1)]

    for x, y, cost in fares:
        cost_board[x][y] = cost
        cost_board[y][x] = cost

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    cost_board[i][j] = 0
                # cost_board[i][j] = min(cost_board[i][j], cost_board[i][k] + cost_board[k][j])
                elif cost_board[i][j] > cost_board[i][k] + cost_board[k][j]:
                    cost_board[i][j] = cost_board[i][k] + cost_board[k][j]
    ans = INF
    for start in range(1,n+1):
        ans = min(ans, cost_board[start][s] + cost_board[start][a]+cost_board[start][b])
    return ans

'''
def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer = INF
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for start, dest, fare in fares:
        graph[start][dest] = fare
        graph[dest][start] = fare
    
    for i in range(1, n + 1):
        graph[i][i] = 0

    # 플로이드 워셜 알고리즘
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, n + 1):
        cost = graph[s][i] + graph[i][a] + graph[i][b]
        answer = min(answer, cost)    

    return answer
'''
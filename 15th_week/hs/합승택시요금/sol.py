import heapq


def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer = INF
    graph = [[] * (n + 1) for _ in range(n + 1)]

    for fare in fares:
        node1, node2, cost = fare
        graph[node1].append((node2, cost))
        graph[node2].append((node1, cost))

    def dijkstra(s):
        q = []
        distance = [INF] * (n + 1)
        heapq.heappush(q, (0, s))
        distance[s] = 0

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue

            for g in graph[now]:
                cost = dist + g[1]
                if cost < distance[g[0]]:
                    distance[g[0]] = cost
                    heapq.heappush(q, (cost, g[0]))
        return distance

    distance_list = [[]] + [dijkstra(i) for i in range(1, n + 1)]

    for i in range(1, n + 1):
        answer = min(distance_list[s][i] + distance_list[i][a] + distance_list[i][b], answer)

    return answer

# def solution(n, s, a, b, fares):
#     INF = int(1e9)
#     answer = INF
#     graph = [[INF] * n for _ in range(n)]

#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 graph[i][j] = 0

#     for fare in fares:
#         node1, node2, cost = fare
#         graph[node1 - 1][node2 - 1] = cost
#         graph[node2 - 1][node1 - 1] = cost

#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

#     for t in range(n):
#         temp = graph[s - 1][t] + graph[t][a - 1] + graph[t][b - 1]
#         answer = min(temp, answer)

#     return answer




# 전선을 하나씩 끊어보고, 한 쪽만 BFS로 탐색하며 한 쪽 전력망에 속한 송전탑의 개수를 세어보고 남은 송전탑들과 얼마나 차이나는지 비교
from collections import deque


def bfs(start, visited, graph):
    queue = deque([start])
    result = 1
    visited[start] = 1
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                result += 1
                queue.append(i)
                visited[i] = 1
    return result


def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    for start, not_visit in wires:
        visited = [0] * (n + 1)
        visited[not_visit] = 1
        result = bfs(start, visited, graph)
        if abs(result - (n - result)) < answer:
            answer = abs(result - (n - result))
    return answer
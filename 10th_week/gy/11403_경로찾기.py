import sys
sys.stdin = open('input.txt')

'''
플로이드-워셜 알고리즘 : 그래프에서 가능한 모든 노드 쌍에 대해 최단 거리 구함
i에서 바로 j로 가는 것보다 i에서 k 거쳐 j로 가는게 효율적이면 값 갱신
3중 for문 중 경로가 되는 k의 for문이 가장 위에 있어야 누락없음
'''

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
# print(arr)

for k in range(N): #경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

for row in graph:
    for col in row:
        print(col, end = ' ')
    print()
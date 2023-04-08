import sys
sys.stdin = open('input.txt')

#중복하는 수 받을 수 있지만 똑같은 리스트 나오면 한번만 출력
#리스트 개수 2 이상 시 중복값 있으면 그 값은 도출하되 중복값이 없으면 이전에 나왔던 수 제외 후
#다음 수 출력

#prev와 같은 값 나오면 제외
#lst에서 이미 출력된 (visited[i]=true) 값이 나오는 경우 제외

def dfs(depth):
    prev = 0
    if depth == M:
        print(' '.join(map(str, lst)))
        return
    for i in range(N):
        if tmp[i] != prev and visited[i] == False:
            lst.append(tmp[i])
            prev = tmp[i]
            visited[i] = True
            dfs(depth + 1)
            lst.pop()
            visited[i] = False

N, M = map(int, input().split())
tmp = list(map(int, input().split()))
tmp.sort()
lst = []
prev = 0
visited = [False] * N

dfs(0)
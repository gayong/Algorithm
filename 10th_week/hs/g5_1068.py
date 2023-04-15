import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(d):
    tree[d] = False
    for i in range(N):
        if d == tree[i]:
            dfs(i)


N = int(input())
tree = list(map(int, input().split()))
D = int(input())
cnt = 0

dfs(D)

for i in range(N):
    if tree[i] != False and i not in tree:
        cnt += 1

print(cnt)

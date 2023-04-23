import sys
input = sys.stdin.readline

def rightrotate(n, d):
    if n == 4:
        return
    if cycle[n-1][2] != cycle[n][6]:
        temp[n] = 1
        direction[n] = -d
        rightrotate(n+1, -d)
    return

def leftrotate(n, d):
    if n == 1:
        return
    if cycle[n-1][6] != cycle[n-2][2]:
        temp[n-2] = 1
        direction[n-2] = -d
        leftrotate(n-1, -d)
    return

def cal():
    for i in range(4):
        if temp[i]:
            copy_lst = list(cycle[i])
            if direction[i] == 1:
                cycle[i] = [copy_lst[-1]] + copy_lst[:7]
            else:
                cycle[i] = copy_lst[1:] + [copy_lst[0]]
                
cycle = [list(map(int, input().rstrip())) for _ in range(4)]
K = int(input())
for _ in range(K):
    N, dir = map(int, input().split())
    temp = [0, 0, 0, 0]
    direction = [0, 0, 0, 0]
    temp[N-1] = 1
    direction[N-1] = dir
    rightrotate(N, dir)
    leftrotate(N, dir)
    cal()
    

# 계산
result = 0
if cycle[0][0] == 1:
    result += 1
if cycle[1][0] == 1:
    result += 2
if cycle[2][0] == 1:
    result += 4
if cycle[3][0] == 1:
    result += 8
    
print(result)

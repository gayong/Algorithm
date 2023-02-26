import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def divide(arr, N):

    global a1, a2, a3

    cnt_0 = 0
    cnt_1 = 0
    cnt_2 = 0

    for i in arr:
        cnt_0 += i.count('0')
        cnt_1 += i.count('1')
        cnt_2 += i.count('-1')

    if cnt_0 == N*N:
        a1 += 1
        return
    elif cnt_1 == N*N:
        a2 += 1
        return
    elif cnt_2 == N*N:
        a3 += 1
        return
    
    k = N//3

    for i in range(0, N, k):
        for j in range(0, N, k):
            new_arr = [[0]*k for _ in range(k)]
            for a in range(k):
                for b in range(k):
                    new_arr[a][b] = arr[i+a][j+b]
            divide(new_arr, k)

N = int(input())

arr = [input().split() for _ in range(N)]
a1, a2, a3 = 0, 0, 0
divide(arr, N)
print(a3)
print(a1)
print(a2)
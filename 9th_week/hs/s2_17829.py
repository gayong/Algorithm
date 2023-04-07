import sys
input = sys.stdin.readline

def devide(arr, N):
    if N == 1:
        print(arr[0][0])
        return
    new_arr = [[] for _ in range(N//2)]
    for i in range(0, N, 2):
        for j in range(0, N, 2):
            new_arr[i//2].append(sorted([arr[i][j], arr[i][j+1], arr[i+1][j], arr[i+1][j+1]])[2])
    return devide(new_arr, N//2)
    

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
devide(arr, N)
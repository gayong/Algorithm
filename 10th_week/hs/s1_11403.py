import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for a in range(N):
        for b in range(N):
            if arr[a][k] and arr[k][b]:
                arr[a][b] = 1

for a in range(N):
    for b in range(N):
        print(arr[a][b], end=" ")
        # if arr[a][b] == 0:
        #     print(0, end=" ")
        # else:
        #     print(1, end=" ")
    print()

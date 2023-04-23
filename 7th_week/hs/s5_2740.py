import sys
input = sys.stdin.readline

N1, M1 = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(N1)]
N2, M2 = map(int, input().split())
arr2 = [list(map(int, input().split())) for _ in range(N2)]

result = [[0]*M2 for _ in range(N1)]

for i in range(N1):
    for j in range(M2):
        temp = 0
        for k in range(N2):
            temp += (arr1[i][k]*arr2[k][j])
        result[i][j] = temp

for i in result:
    print(*i)

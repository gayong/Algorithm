import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
# print(A)

M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]
# print(B)

C = [[0 for _ in range(K)] for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            C[n][k] += A[n][m] * B[m][k]

for i in C:
    for j in i:
        print(j, end=' ')
    print()

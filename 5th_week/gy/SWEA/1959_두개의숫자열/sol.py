import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #N은 짧은놈 길이, M은 긴놈 길이
    aj = list(map(int, input().split())) #짧은놈
    bj = list(map(int, input().split())) #긴놈
    if N > M:
        N, M, aj, bj = M, N, bj, aj

    rlt = []
    for i in range(M-N+1):
        mul = 0
        for j in range(N):
            mul += aj[j] * bj[i+j]
        rlt.append(mul)
    print(f'#{tc} {max(rlt)}')

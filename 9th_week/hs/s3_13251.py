import sys
input = sys.stdin.readline

M = int(input())
N = list(map(int, input().split()))
K = int(input())

if M == 1 or K == 1:
    print(1.0)
else:
    ans = 0
    total = sum(N)
    for i in range(M):
        total2 = 1
        for j in range(K):
            total2 *= ((N[i]-j)/(total-j))
        ans += total2
    print(ans)

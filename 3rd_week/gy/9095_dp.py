#정수 N < 11
#N을 1,2,3의 합으로 나타내는 방법의 수 구하기
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    dp = [0, 1, 2, 4]
    for i in range(4, 12):
        dp.append(sum(dp[-3:]))
    print(dp[N])




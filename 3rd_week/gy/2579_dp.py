#계단오르기 - 계단 한 칸 or 두 칸씩 가능 / 연속 세 칸 이상 X / 마지막 계단은 꼭 밟아야 함 >> 점수 최대값
import sys
input = sys.stdin.readline

T = int(input())
stair = [int(input()) for _ in range(T)]
dp = []

if len(stair) <= 2:
    print(sum(stair))
else:
    dp.append(stair[0])
    dp.append(stair[0] + stair[1])
    dp.append(max(stair[0] + stair[2], stair[1] + stair[2]))
    for i in range(3, T):
        dp.append(max(dp[i-3] + stair[i] + stair[i-1], dp[i-2] + stair[i]))
    print(dp.pop()) #print(dp[T-1])
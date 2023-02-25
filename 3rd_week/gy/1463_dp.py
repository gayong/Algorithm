import sys
input = sys.stdin.readline

N = int(input())

#1-----------------------------------------------------------
dp = [0] * (N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
print(dp[N])

#2-----------------------------------------------------------
def sum_dp(N):
    dp2 = [0,0,1,1]  #N은 1부터지만 인덱스 맞추기용
    for i in range(4, N+1):
        dp2.append(dp2[i-1]+1)    #일단 dp[i-1]+1값 넣어주고
        if i % 3 == 0:          #비교하면서 dp[i//3]+1 값이 더 작다면 바꿔줌
            dp2[i] = min(dp2[i], dp2[i//3]+1)
        if i % 2 == 0:
            dp2[i] = min(dp2[i], dp2[i//2]+1)
    return dp2[N]

print(sum_dp(N))
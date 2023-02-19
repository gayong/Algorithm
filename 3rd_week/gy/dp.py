def stair_dp(N):
    dp = [0,1,2]
    for i in range(3, N+1):
        dp.append(dp[i-1]+dp[i-2])
    return dp[N]

print(stair_dp(4))

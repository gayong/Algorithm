#피보나치
# def fib(n):
#     now, next = 0, 1
#     for _ in range(n):
#         now, next = next, now + next
#     return now

# N = int(input())
# print(fib(N))

def fib_dp(num):
    dp = [0, 1]
    for i in range(2, num+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[-1]

N = int(input())
print(fib_dp(N))
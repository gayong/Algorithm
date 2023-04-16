import sys
input = sys.stdin.readline

N = int(input())
result = [[1,1,1,1,1,1,1,1,1,1]] + [[0,0,0,0,0,0,0,0,0,0] for _ in range(N-1)]

for i in range(1, N):
    for j in range(10):
        total = 0
        for k in result[i-1][:j+1]:
            total += k
        result[i][j] = total
temp = 0
for i in result[-1]:
    temp += i

print(temp%10007)

# n = int(input())
# dp = [1]*10

# for i in range(n-1):
#     for j in range(1, 10):
#         dp[j] += dp[j-1]
        
# print(sum(dp)%10007)

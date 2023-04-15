import sys
input = sys.stdin.readline

N = int(input())
nums = sorted(list(map(int, input().split())))
cnt = 0
x = int(input())
start, end = 0, N-1
while start < end:
    total = nums[start] + nums[end]
    if total == x:
        cnt += 1
        start += 1
    elif total > x:
        end -= 1
    else:
        start += 1
print(cnt)
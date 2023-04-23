import sys
sys.stdin = open('input.txt')

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
x = int(input())

start, end = 0, n - 1
cnt = 0
while start < end:
    if arr[start] + arr[end] < x:
        start += 1
        continue
    if arr[start] + arr[end] == x:
        cnt += 1
    end -= 1
print(cnt)

# 왜 둘 다 0에서 시작하는 투포인터는 안되는걸까??

# end = 0
# cnt = 0
# interval_sum = 0
# # start 차례로 증가시키며 반복
# for start in range(n):
#     # end 끝까지 이동시키며 탐색
#     while interval_sum < x and end < n:
#         interval_sum += nums[end]
#         end += 1
#     # 부분합 x되면 cnt 증가하기
#     if interval_sum == x:
#         cnt += 1
#     interval_sum -= nums[start]
#
# print(cnt)
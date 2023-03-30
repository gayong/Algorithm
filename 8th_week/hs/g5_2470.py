import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

left, right = 0, N-1
INF = 1e10
while left < right:
    arr_l = arr[left]
    arr_r = arr[right]
    diff = arr_l+arr_r
    if abs(diff) < INF:
        INF = abs(diff)
        ans = (arr_l, arr_r)
    if diff == 0:
        break
    elif diff < 0:
        left += 1
    else:
        right -= 1

print(*ans)
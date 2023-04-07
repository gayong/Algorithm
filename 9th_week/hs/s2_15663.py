import sys
input = sys.stdin.readline

def check(temp, n):
    if n == M:
        print(*temp)
        return
    used = 0
    for i in range(target):
        if visited[i]:
            continue
        if used == nums[i]:
            continue
        temp.append(nums[i])
        used = nums[i]
        visited[i] = 1
        check(temp, n+1)
        temp.pop()
        visited[i] = 0

N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))
target = len(nums)
visited = [0] * target
temp = []
check(temp, 0)

# import sys
# input = sys.stdin.readline

# def check(temp, n):
#     global result
#     info = temp[:]
#     if info in result[n]:
#         return
#     else:
#         result[n].append(info)
#     if n == M:
#         print
#         return
#     for i in range(target):
#         if visited[i]:
#             continue
#         origin = temp[:]
#         temp.append(nums[i])
#         visited[i] = 1
#         check(temp, n+1)
#         temp = origin[:]
#         visited[i] = 0

# N, M = map(int, input().split())

# nums = sorted(list(map(int, input().split())))
# target = len(nums)
# visited = [0] * target
# result = [[] for _ in range(M+1)]
# temp = []
# check(temp, 0)
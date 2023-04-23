import sys
from collections import deque
input = sys.stdin.read

H, W, *rain = map(int, input().split())
result = 0
for i in range(1, W-1):
    left = max(rain[:i])
    right = max(rain[i+1:])
    height = min(left, right)
    
    if rain[i] < height:
        result += (height-rain[i])
print(result)

# H, W, stack, *q = map(int, input().split())
# stack = [stack]
# q = deque(q)

# result = 0
# for i in range(W-2):
#     here = q.popleft()
#     height = min(max(stack), max(q))
#     if height > here:
#         result += (height-here)
#     stack.append(here)
    
# print(result)

#NxM 수열
import sys
import itertools

input = sys.stdin.readline

N, M = map(int, input().split())

nums = [ i for i in range(1,N+1) ]

result = list(itertools.permutations(nums, M))


for ans in result:
    print(*ans)
    
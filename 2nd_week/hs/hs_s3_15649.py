from itertools import permutations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

for i in permutations(range(1, N+1), M):
    for j in range(M):
        print(i[j], end=" ")
    print()

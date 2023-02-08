import sys

input = sys.stdin.readline

N = int(input())
numbers = sorted(list(set(map(int, input().split()))))
print(*numbers)

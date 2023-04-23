import sys
input = sys.stdin.readline

T = int(input().rstrip())
N = set(map(int, input().split()))
t = int(input().rstrip())
M = list(map(int, input().split()))

for i in M:
    if i in N:
        print(1)
    else:
        print(0)

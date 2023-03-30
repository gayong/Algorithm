import sys
input = sys.stdin.readline

N = int(input())


def move(n, a, b, c):
    if n == 0:
        return
    move(n-1, a, c, b)
    print(a, b)
    move(n-1, c, b, a)


print(2**N - 1)
move(N, 1, 3, 2)

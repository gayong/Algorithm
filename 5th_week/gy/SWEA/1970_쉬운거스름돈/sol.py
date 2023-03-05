import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N = N - (N % 10)

    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    lst = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        lst[i] = N // money[i]
        N = N - (money[i] * lst[i])

    print(f'#{tc}')
    print(*lst)

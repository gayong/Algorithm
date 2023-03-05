import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # print(arr)

    y = 99
    for i in range(100):
        if arr[y][i] == 2:
            x = i
    # print(x)

    while True:
        if y == 0:
            break
        if x > 0 and arr[y][x-1] == 1:
            while x > 0 and arr[y][x-1] == 1:
                x -= 1
            else:
                y -= 1
        elif x < 99 and arr[y][x+1] == 1:
            while x < 99 and arr[y][x+1] == 1:
                x += 1
            else:
                y -= 1
        else:
            y -= 1

    print(f'#{tc} {x}')
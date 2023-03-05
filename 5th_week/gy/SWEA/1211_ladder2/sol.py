import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # print(arr)

    start = []

    for i in range(100):
        if arr[0][i] == 1:
            start.append(i)
    # print(start)
    # start = x

    ans = []
    for st in start:
        cnt = 0
        y = 99
        while True:
            if y == 0:
                break
            if st > 0 and arr[y][st - 1] == 1:
                while st > 0 and arr[y][st - 1] == 1:
                    st -= 1
                    cnt += 1
                else:
                    y -= 1
                    cnt += 1
            elif st < 99 and arr[y][st + 1] == 1:
                while st < 99 and arr[y][st + 1] == 1:
                    st += 1
                    cnt += 1
                else:
                    y -= 1
                    cnt += 1
            else:
                y -= 1
                cnt += 1
        ans.append((cnt, st))

    print(f'#{tc} {min(ans)[1]}')
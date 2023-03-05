import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input()) #덤프 횟수
    box = list(map(int, input().split())) #상자 높이값
    box.sort()

    while N > 0:
        box[-1] = box[-1] - 1
        box[0] = box[0] + 1
        box.sort()
        N -= 1
    ans = max(box)-min(box)
    print(f'#{tc} {ans}')
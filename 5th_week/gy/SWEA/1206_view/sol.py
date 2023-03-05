import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input()) #건물 개수
    lst = list(map(int, input().split()))

    cnt = 0
    for i in range(2, N-2):
        if lst[i] > lst[i-1] and lst[i] > lst[i-2] and lst[i] > lst[i+1] and lst[i] > lst[i+2]:
            neighbor_max = max(lst[i-1], lst[i-2], lst[i+1], lst[i+2])
            cnt += lst[i] - neighbor_max
    print(f'#{tc} {cnt}')

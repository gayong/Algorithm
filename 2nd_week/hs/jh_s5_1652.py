import sys

input = sys.stdin.readline

N = int(input())

room = [input().rstrip() for _ in range(N)]

row_cnt = 0
col_cnt = 0
for i in range(N):
    cnt = 0
    for j in room[i]:
        if j == '.':
            cnt += 1
        else:
            if cnt >= 2:
                row_cnt += 1
            cnt = 0
    if cnt >= 2:
        row_cnt += 1

    temp = [row[i] for row in room]
    temp2 = ''
    for j in range(N):
        temp2 += temp[j]
    cnt = 0
    for j in temp2:
        if j == '.':
            cnt += 1
        else:
            if cnt >= 2:
                col_cnt += 1
            cnt = 0
    if cnt >= 2:
        col_cnt += 1

print(row_cnt, col_cnt)

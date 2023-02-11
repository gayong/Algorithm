#체스판 다시 칠하기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
check = [input() for _ in range(N)]         #['WBWBWBWB','BWBWBWBW', ...]
# print(check)
count = []

for i in range(N-7):    #체스판 칠할 부분 찾는 시작점
    for j in range(N-7):
        #8개씩 조사하기 시작하는데
        # 시작점 바뀔때마다 첨부터 칠함
        color1 = 0  # 시작지점 검은색인 경우
        color2 = 0  # 시작지점 흰색인 경우
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if check[k][l] != 'W':
                        color1 += 1
                    if check[k][l] != 'B':
                        color2 += 1
                else:
                    if check[k][l] != 'B':
                        color1 += 1
                    if check[k][l] != 'W':
                        color2 += 1
        count.append(min(color1, color2))

print(min(count))

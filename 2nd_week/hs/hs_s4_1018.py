import sys

input = sys.stdin.readline

N, M = map(int, input().split())
chessboard = [list(map(str, input().rstrip())) for _ in range(N)]
count = []
for i in range(N-7):
    for j in range(M-7):
        cnt1 = 0
        cnt2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if chessboard[a][b] != 'W':
                        cnt1 += 1
                    if chessboard[a][b] != 'B':
                        cnt2 += 1
                else:
                    if chessboard[a][b] != 'B':
                        cnt1 += 1
                    if chessboard[a][b] != 'W':
                        cnt2 += 1
        count.append(cnt1)
        count.append(cnt2)

print(min(count))

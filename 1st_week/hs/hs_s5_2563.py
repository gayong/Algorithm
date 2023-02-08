import sys
input = sys.stdin.readline

N = int(input().rstrip())
paper_width = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper_width[i][j] = 1

width = 0
for row in paper_width:
    width += row.count(1)
print(width)

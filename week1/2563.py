#색종이
import sys
input = sys.stdin.readline

T = int(input().rstrip())

# rows = 100
# cols = 100
# arr = [[0 for j in range(cols)] for i in range(rows)]       #0으로 찬 이차행렬 만들기
# 파이썬엔 array 없으니 다른 변수명 사용
paper = [[0] * 100 for _ in range(100)]

for k in range(T):
    row, col = map(int, input().rstrip().split())           #세로, 가로
    for l in range(row, row+10):                            #색종이 붙인 영역
        for m in range(col, col+10):                        
            paper[l][m] = 1                                   #1로 값 바꿔줌

count = 0
for x in paper:
    count += x.count(1)                                     #1 세기

print(count)

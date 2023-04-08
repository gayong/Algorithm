import sys
sys.stdin = open('input.txt')

def promising(x):
    for i in range(x):
        #열이 같거나 대각선이 같으면(두 좌표에서 행-행 = 열-열) false
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return
    else:
        #각 행에 퀸 놓음
        for i in range(n): #열번호 0~N전까지 옮기며 유망한 곳 찾기
            # [x, i]에 퀸을 놓음
            row[x] = i
            if promising(x): #행,열,대각선 체크함수 true면 백트래킹 안하고 계속 진행
                n_queens(x + 1)

n = int(input())

ans = 0
row = [0] * n
n_queens(0)
print(ans)
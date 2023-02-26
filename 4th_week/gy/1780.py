import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')

def cut(x, y, n):
    global minus, zero, plus
    num = paper[x][y]  # 첫 번째 숫자

    for i in range(x, x + n):
        for j in range(y, y + n):
            if num != paper[i][j]:
                cut(x, y, n // 3)
                cut(x, y + n // 3, n // 3)
                cut(x, y + n // 3 * 2, n // 3)
                cut(x + n // 3, y, n // 3)
                cut(x + n // 3, y + n // 3, n // 3)
                cut(x + n // 3, y + n // 3 * 2, n // 3)
                cut(x + n // 3 * 2, y, n // 3)
                cut(x + n // 3 * 2, y + n // 3, n // 3)
                cut(x + n // 3 * 2, y + n // 3 * 2, n // 3)
                return
    if num == -1:
        minus += 1
    elif num == 0:
        zero += 1
    elif num == 1:
        plus += 1


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

minus, zero, plus = 0, 0, 0
cut(0, 0, N)
print(minus, zero, plus, sep='\n')

#####################################
# 종이 종류 RESULT
result = {-1:0, 0:0,1:0}

# 2. 종이의 종류(-1, 0, 1)와 다르면 분할
def divided(row,col,n):
    curr = paper[row][col] # 종이의 시작

    for i in range(row, row+n):
        for j in range(col, col+n):
            # 현재 종이 종류와 다르다면
            if paper[i][j] != curr:
                # 종이 1/3로 분할 (ex. n == 9 , n = 9 -> 3 -> 1 )
                next = n//3
                # 종이를 같은 크기의 종이 9개로 자르므로
                divided(row, col, next) # 1번째 block (0,0)
                divided(row, col+next, next) # 2번째 block (0,1)
                divided(row, col+(next*2), next) # 3번째 block (0,2)
                divided(row+next, col, next) # 4번째 block (1,0)
                divided(row+next, col+next, next) # 5번째 block (1,1)
                divided(row+next, col+(next*2), next) # 6번째 block (1,2)
                divided(row+(next*2), col, next) # 7번째 block (1,0)
                divided(row+(next*2), col+next, next) # 8번째 block (1,1)
                divided(row+(next*2), col+(next*2), next) # 9번째 block (1,2)
                return

    # 3. 종이 종류에 따라 count
    result[curr] +=1
    return


divided(0,0,n)

# 4. 결과 return
for i in result.values():
    print(i)
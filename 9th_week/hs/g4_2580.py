import sys
input = sys.stdin.readline

def checkRow(x, n):
    for i in range(9):
        if n == arr[x][i]:
            return False
    return True

def checkCol(y, n):
    for i in range(9):
        if n == arr[i][y]:
            return False
    return True

def checkSquare(x, y, n):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if n == arr[nx+i][ny+j]:
                return False
    return True

def solution(n, target):
    if n == target:
        for i in range(9):
            print(*arr[i])
        exit(0)

    for i in range(1, 10):
        x = space[n][0] 
        y = space[n][1] 

        if checkRow(x, i) and checkCol(y, i) and checkSquare(x, y, i):
            arr[x][y] = i
            solution(n + 1, target)
            arr[x][y] = 0


arr = []
space = []
for i in range(9):
    arr.append(list(map(int, input().split())))
    for j in range(9):
        if arr[i][j] == 0:
            space.append((i, j))
target = len(space)
solution(0, target)
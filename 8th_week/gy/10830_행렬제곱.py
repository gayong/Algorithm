import sys
input = sys.stdin.readline

def matrix_mul(mat_a, mat_b):
    length = len(mat_a)
    temp = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                temp[i][j] += mat_a[i][k] * mat_b[k][j]
            temp[i][j] %= 1000
    return temp


def matrix_pow(original, n):
    if n == 1:
        return original
    if n % 2 == 0:
        temp = matrix_pow(original, n // 2)
        return matrix_mul(temp, temp)
    else:
        temp = matrix_pow(original, n - 1)
        return matrix_mul(temp, original)


read = sys.stdin.readline
N, M = map(int, read().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = matrix_pow(matrix, M)
for row in result:
    for num in row:
        print(num % 1000, end=' ')
    print()
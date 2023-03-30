import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        arr[i][j] = arr[i][j] % 1000

#행렬을 n 번 곱한 값을 save[n]에 저장
save = dict()
save[1] = arr

def multiple(n, m):
    # 행렬을 m번 연산한 값이 이미 저장되어있으면 바로 return
    if m in save:
        return save[m]
    else:
        #저장되어있지 않을 경우 더 작은 값에 대해 재귀 호출을 한다.
        lista = multiple(n, m//2)
        listb = multiple(n, m-m//2)
        arr = list([0 for _ in range(n)] for _ in range(n))

        for i in range(n):
            for j in range(n):
                arr[i][j] = 0
                for x in range(n):
                    arr[i][j] += lista[i][x] * listb[x][j]
                arr[i][j] %= 1000

        save[m] = arr
        return save[m]
#출력
for x in multiple(n, m):
    for i in x:
        print(i, end=' ')
    print()
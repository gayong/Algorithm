import sys
sys.stdin = open('input.txt')

#좌상단, 우상단, 좌하단, 우하단으로 나눠 배열크기 2가 될때까지 나누고 그 중 두번째로 큰 수 저장
def pooling(size, x, y):
    mid = size//2

    #첨부터 주어진 행, 열 2면 그냥 두번째로 큰 수만 뺌
    if size == 2:
        ans = [nums[x][y], nums[x+1][y], nums[x][y+1], nums[x+1][y+1]]
        ans.sort()
        return ans[-2]

    lt = pooling(mid, x, y)
    rt = pooling(mid, x+mid, y)
    lb = pooling(mid, x, y+mid)
    rb = pooling(mid, x+mid, y+mid)
    ans = [lt, rt, lb, rb] #재귀 처리 후 최종으로 가져온 값들
    ans.sort()
    return ans[-2]

n = int(input())
nums = []
for i in range(n):
    tmp = list(map(int, input().split()))
    nums.append(tmp)

print(pooling(n, 0, 0))
#좌표 정렬하기
import sys
input = sys.stdin.readline

N = int(input())

a = [list(map(int, input().split())) for n in range(N)]
a.sort(key = lambda x: (x[0], x[1]))

for i in range(len(a)):
    print(*a[i])
    
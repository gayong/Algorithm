import sys

input = sys.stdin.readline

N = int(input())

point_list = [tuple(map(int, input().split())) for _ in range(N)]

point_list.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    print(f'{point_list[i][0]} {point_list[i][1]}')

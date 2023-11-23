#소수 개수 구하기
import sys
input = sys.stdin.readline

T = int(input())

line = list(map(int, input().rstrip().split()))

count = 0
for num in line:
    if num == 1:
        continue
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        count += 1
    # if num == 2:
    #     count += 1
    # else:
    #     div = []
    #     for idx in range(2, num):
    #         if num % idx != 0:
    #             div.append(idx) #나머지가 0이 아닌 나눔수들(2, 자기자신 제외)
    #             if len(div) == num - 2:
    #                 count += 1

print(count)

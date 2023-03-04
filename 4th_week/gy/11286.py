#절댓값 힙
import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')

import heapq

N = int(input())
heap = []
for _ in range(N):
    num = int(input())
    if num == 0:
        try:
            print(heapq.heappop(heap)[1]) #꺼내오는건 튜플 속 원본 1번 인덱스
        except:
            print(0)
    else: #숫자가 주어진 경우 힙에 추가하는데
        heapq.heappush(heap, (abs(num), num)) #튜플일땐 맨 앞 숫자로 정렬함




#최대힙
import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')

#heapq 사용
import heapq
N = int(input())
heap = []
for _ in range(N):
    i = int(input())
    if i == 0:
        try:
            print(-1 * heapq.heappop(heap)) #빼올때도 - 다시 붙여 양수값으로 만듦
        except:
            print(0) #비어있는데 0인 경우
    else:
        heapq.heappush(heap, -i) #heapq는 최소힙 형태로 정렬되니 -붙여 절댓값 큰수부터 정렬

# def enq(n):
#     global last
#     last += 1
#     heap[last] = n
#     c = last
#     p = c // 2
#     while p > 0 and heap[p] < heap[c]:
#         heap[p], heap[c] = heap[c], heap[p]
#         c = p
#         p = c // 2
#     return
#
# N = int(input())
# heap = [0] * 20
# last = 0
#
# for k in range(N):
#     i = int(input())
#     if i > 0:
#         enq(i)
#     elif i == 0:
#         print(heap.pop(1))


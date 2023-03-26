import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')

N = int(input())
A = set(map(int, input().split()))
#set로 받으면 탐색시간 줄일 수 있음

M = int(input())
arr = list(map(int, input().split()))

for num in arr:
    print(1) if num in A else print(0)
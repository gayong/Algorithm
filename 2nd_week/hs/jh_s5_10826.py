import sys

input = sys.stdin.readline

N = int(input())
fibo_list = [0, 1, 1]

for i in range(3, N+1):
    fibo_list.append(fibo_list[i-1] + fibo_list[i-2])

if N == 0:
    print(0)
else:
    print(fibo_list[-1])

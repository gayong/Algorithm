import sys

input = sys.stdin.readline

num1, num2 = map(int, input().split())

for i in range(1, min(num1, num2)+1):
    if num1 % i == 0 and num2 % i == 0:
        result = i

print(result, num1*num2//result)

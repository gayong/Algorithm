#한수
import sys
input = sys.stdin.readline

N = int(input())

if N <= 99:
    print(N)
elif 100 <= N < 1000:
    count = 99
    for num in range(100, N+1):
        # a = []
        # for i in str(num):
            # a.append(int(i)) 대신 list comprehension으로 간단하게
        a = [ int(i) for i in str(num) ]
        if a[1] - a[0] == a[2] - a[1]:
            count += 1
        num += 1
    print(count)
else:
    print(144)


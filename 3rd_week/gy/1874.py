#스택수열
import sys
input = sys.stdin.readline

N = int(input().rstrip())
now = 1
stack = []
a = []
ans = True

for i in range(N):
    num = int(input().rstrip())
    while now <= num:
        stack.append(now)
        a.append('+')
        now += 1
    if stack[-1] == num:
        stack.pop()
        a.append('-')
    else:   #출력초과 계속 뜬게 no만 나오지않고 +-값들도 같이 나와서같음
        ans = False

if not ans:
    print('NO')
else:
    for i in a:
        print(i)


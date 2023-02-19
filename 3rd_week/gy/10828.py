# 스택
import sys
input = sys.stdin.readline

N = int(input())
stack = []
for i in range(N):
    ins = input().rstrip()
    if 'push' in ins:
        num = int(ins.split()[-1])
        stack.append(num)
    elif ins == 'pop':
        if stack:
            pop = stack.pop()
            print(pop)
        else:
            print(-1)
    elif ins == 'size':
        print(len(stack))
    elif ins == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif ins == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)


#괄호 체크
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    word = input()
    result = 'YES'
    stack = []
    for char in word:
        if char == '(':
            stack.append(char)
        else:
            if char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                elif not stack:
                    result = 'NO'
                    break
                elif stack[-1] != '(':
                    result = 'NO'
                    break
    if stack:
        result = 'NO'
    print(result)



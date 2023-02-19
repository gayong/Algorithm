#균형잡힌 세상
import sys
input = sys.stdin.readline  #아예 이 두 줄 다 지우고 s도 input으로만 받으면 출력초과 안뜸

while 1:
    s = sys.stdin.readline().rstrip()   #rstrip 안하면 출력초과
    if s == '.':
        break

    stack = []
    result = 'yes'
    for char in s:
        if char == '(' or char == '[':
            stack.append(char)
        else:
            if char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                elif not stack:
                    result = 'no'
                    break
                elif stack[-1] != '(':
                    result = 'no'
                    break
            if char == ']':
                if not stack or stack[-1] != '[':
                    result = 'no'
                    break
                else:
                    stack.pop()
    if stack:
        result = 'no'

    print(result)

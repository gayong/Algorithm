# 균형잡힌 세상
import sys
# sys.stdin = i
input = sys.stdin.readline

# 몇개씩 들어오는지 모른다..
while True:
    sentences = input().rstrip()
    if len(sentences) == 1 and sentences[0] == ".":
        break
    result = 'yes'
    stack = []
    for char in sentences:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = 'no'
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                result = 'no'
        else:
            continue

    else:
        if stack:
            result = 'no'

    print(result)
# ()). 입력시 )얘가 안들어와서 yes가 되어버렸다.......

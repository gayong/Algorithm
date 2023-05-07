'''
올바른 괄호 문자열인지 판단 => '(' 가 나오면 stack에 넣어주고, ')'가 나왔을 때,
스택이 비어있는지 아닌지 체크하는 것이다. 비어있다면 올바르지 않은 괄호 문자열임,,,
u랑 v로 쪼개고 u가 올바른/올바르지않은 문자열인지 판단하는 함수1
올바르게 변환해주는 함수2
'''

def split(p):
    stack = []
    left = 0
    right = 0
    flag = True
    for i, pp in enumerate(p): # 인덱스랑 요소
        # print(i, pp)
        if pp == '(':
            left += 1
            stack.append('(')
        else:
            right += 1
            if len(stack) == 0:
                flag = False
            else: # 올바른 괄호면?
                stack.pop() # ( 삭제해서 한 쌍 제거
        # u가 균형잡힌 문자열이 되려면 left, right 괄호 수가 같아지는 첫 순간
        if left == right:
            return i+1, flag # v의 시작 인덱스, u의 올바른 괄호 문자열 여부 전달

def solution(p):
    #1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if len(p) == 0:
        return p
    #2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    v_idx, u_correct = split(p)
    u = p[:v_idx]
    v = p[v_idx:]
    #3 u가 올바른이면
    if u_correct == True:
        #3-1 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
        return u + solution(v)
    #4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    else:
        #4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        #4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 문자열 이어붙입니다.
        #4-3. ')'를 다시 붙입니다.
        answer = '(' + solution(v) + ')'

        #4-4 u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        for i in range(1, len(u)-1):
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('

        #4-5 생성된 문자열을 반환합니다.
        return answer
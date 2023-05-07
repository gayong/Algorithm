def solution(p):
    if not p :
        return p

    isCorrect = True
    v = 0
    for i in range(len(p)):
        if p[i] == '(':
            v -= 1
        else:
            v += 1
            
        if v > 0:
            isCorrect = False
        
        if v == 0:
            if isCorrect:
                return p[:i + 1] + solution(p[i + 1:])
            else:
                return '(' + solution(p[i + 1:]) + ')' + ''.join(list(map(lambda x: '(' if x == ')' else ')', p[1:i])))

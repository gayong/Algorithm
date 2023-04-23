def solution(routes):
    answer = 0
    routes.sort(key = lambda x:x[1])
    length = len(routes)
    left = -30001
    for i in routes:
        if i[0] > left:
            left = i[1]
            answer += 1
            
    return answer
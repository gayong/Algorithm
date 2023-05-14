def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for b in range(1, total+1):
        if not (total % b): 
            a = total // b
            if a >= b:
                if 2*a + 2*b == brown + 4:
                    return [a, b]
    return answer

print(solution(8, 1))
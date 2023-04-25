def solution(A, B):
    answer = 0
    length = len(A)
    A.sort()
    B.sort()
    idx = 0
    for i in range(length):
        while True:
            if idx == length:
                break 
            if A[i] < B[idx]:
                answer += 1
                idx += 1
                break
            else:
                idx += 1
        if idx == length:
            break 
    return answer
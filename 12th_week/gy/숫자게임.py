# A, B 정렬
# A팀 기준으로 반복
# 현재 A팀 인원과 B팀 인원 비교, B가 더 크면 ans+=1, B인덱스+=1
# 만약 B가 더 작으면 B인덱스 높여서 비교 (B인덱스 끝날때까지)

def solution(A, B):
    answer = 0

    A.sort()
    B.sort()

    b_idx = 0
    for a in A:
        while b_idx < len(B):
            if B[b_idx] > a:
                answer += 1
                b_idx += 1
                break
            b_idx += 1
    return answer
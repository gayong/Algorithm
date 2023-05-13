# 정확성만 다 통과하고 시간초과 뜸 ㅠㅅ ㅠ

def solution(stones, k):
    ans = 0  # 건널 수 있는 사람 수
    while True:
        ans += 1
        for i in range(len(stones)):
            if stones[i] == 0:  # 그 칸이 0이면 밑에 for문으로
                continue
            else:  # 아니라면 뛸 때마다 -1씩
                stones[i] -= 1

        cnt = 0  # 연속된 0의 개수 세기 위한 cnt
        for stone in stones:
            if stone == 0:
                cnt += 1
                if cnt == k:  # k개랑 같아지면
                    return ans  # 건널 수 있는 사람 수 리턴
            else:
                cnt = 0
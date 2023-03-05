import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) #N개 과목중 K개 선택
    score = list(map(int, input().split()))
    score.sort(reverse=True)

    sum_score = 0
    for i in range(K):
        sum_score += score[i]

    print(f'#{tc} {sum_score}')
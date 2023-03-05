import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) #N 전체수강생 / K 낸 사람 수
    hw = list(map(int, input().split())) #낸 사람 번호

    all = [i for i in range(1, N+1)]

    ans = []
    for st in all:
        if st not in hw:
            ans.append(st)
    print(f'#{tc}', *ans)
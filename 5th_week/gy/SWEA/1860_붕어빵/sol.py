import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    # N: 사람수, M초의 시간을 들이면 K개의 붕어 만들수있음
    N, M, K = map(int, input().split())
    ppl = list(map(int, input().split()))
    ppl.sort()
    result = "Possible"

    sold_fish = 0
    for p in ppl:
        made_fish = (p // M) * K # p초까지 만들어진 붕어 개수: (p // M) * K

        remain = made_fish - sold_fish # 팔고 남은 붕어빵
        if remain <= 0:
            result = 'Impossible'
            break
        else:
            sold_fish += 1 # 하나 팔때마다 +1

    print("#{} {}".format(tc, result))

import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    mag = [list(map(int, input().split())) for _ in range(100)] #가로

    magg = list(zip(*mag))      #일단 세로로 zip하기 (전치행렬됨)
    ans = 0
    for tp in magg:             #튜플 형태기 때문에
        a = list(tp)            #리스트로 바꿔준담에
        while 0 in a:           #그 속 0을 다 지워줌
            a.remove(0)         #모든 0을 지우기 위해선 반복문 필요
        while a[0] == 2:        #1(N)극에 붙어있는 2의 경우 테이블 아래로 떨어지니
            a.pop(0)            #다 삭제
        while a[-1] == 1:       #2(S)극에 붙어있는 1의 경우 테이블 아래로 떨어지니
            a.pop(-1)           #다 삭제
        b = ''
        for n in a:             #남은애들만 다
            b += str(n)         #문자열 만들어준담에
        ans += b.count('12')    #거기서 이제 '12'의 개수를 세줌(교착덩어리)
    print(f'#{tc} {ans}')

    # for st in zip(*mag):
    # ans += ''.join(st).replace('0','').count('12')
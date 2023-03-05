import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]
    # print(lst)

    all = []
    for i in range(100):
        garo = 0
        sero = 0
        for j in range(100):
            garo += lst[i][j]
            sero += lst[j][i]
        all.append(garo)
        all.append(sero)
    # print(all)

    for i in range(100):
        dae = 0
        dae += lst[i][i]
    all.append(dae)

    #4,0 3,1
    #0,0 1,1 2,2 3,3 4,4
    for j in range(100):
        dae2 = 0
        dae2 += lst[j][99-j]
    all.append(dae2)

    print(f'#{tc} {max(all)}')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, list(input().strip()))) for _ in range(N)]

    m = N // 2  # 중심
    answer = 0
    for i in range(m+1):  # 위아래가 대칭이므로 절반까지
        for j in range(m - i, m + i + 1):  # 중심을 기준으로 왼쪽으로 1칸, 오른쪽으로 1칸 범위를 늘려 나간다.
            answer += farm[i][j] + farm[N-i-1][j]

    print(f'#{test_case} {answer - sum(farm[m])}')  # 가운데를 두번 더해줬으니 함 빼줘야됨!!!!!!

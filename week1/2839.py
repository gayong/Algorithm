#설탕봉지
N = int(input())

div_5 = N // 5                          #5로 나눈 몫을
for i in range(div_5, -1, -1):          #거기서부터 하나씩 내려가면서 순회
    if (N - (5 * i)) % 3 == 0:          #5나 3으로 어째저째 나눠떨어진다면
        div_3 = (N - (5 * i)) // 3      #3키로 봉지를 몇개써야하는지가 나옴
        ans = i + div_3                 #i는 5키로 봉지 개수, div_3은 3키로 봉지개수
        print(ans)                      #더한게 최종 봉지개수
        break
else:                                   #for문 다 도는동안 break를 만나지않는다면
    print(-1)                           #-1
    
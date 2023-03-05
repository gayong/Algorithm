import sys
sys.stdin = open('s_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    # print(nums)

    mul = []
    for i in range(N):
        for j in range(i+1, N):
            if nums[i]*nums[j] >= 10:
                mul.append(str(nums[i]*nums[j]))
    # print(mul)

    ans = []
    for n in mul:
        for j in range(1,len(n)):
            if int(n[j-1]) <= int(n[j]):
                ans.append(n)
    if len(ans) == 0:
        anss = -1
    else:
        anss = max(ans)
    print(f'#{tc} {anss}')


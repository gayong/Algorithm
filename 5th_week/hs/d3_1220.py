import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

for tc in range(1, 11):
    N = int(input())
    # 테이블 위가 N 아래가 S
    # 1은 N 2는 S
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_t = list(map(list,zip(*arr)))
    stack = []
    result = 0
    for i in arr_t:
        cnt = 0
        for j in range(100):
            if i[j] == 1 or i[j] == 2:
                stack.append(i[j])
        while stack:
            temp = stack.pop()
            if temp == 2:
                while stack:
                    if stack.pop() == 1:
                        cnt += 1
                        break
            elif temp == 1:
                pass
        result += cnt

    print(f'#{tc}', result)
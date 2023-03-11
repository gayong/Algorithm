import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for tc in range(1, 11):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            arr_sum = 0
            for k in range(M):
                for l in range(M):
                    arr_sum += arr[i+l][j+k]
            if  result < arr_sum:
                result = arr_sum
    
    print(f'#{tc} {result}')
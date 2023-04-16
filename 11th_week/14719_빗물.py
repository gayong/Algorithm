import sys
sys.stdin = open('0input.txt')
input = sys.stdin.readline

h, w = map(int, input().split())
world = list(map(int, input().split()))

ans = 0
for i in range(1, w - 1):
    left_max = max(world[:i]) # i칸 전까지 중에 젤 큰거
    right_max = max(world[i + 1:]) # i칸 이후부터 젤 큰거

    rain = min(left_max, right_max) # 더 작은값까지 고임

    if world[i] < rain: # i칸이 더 작다면
        ans += rain - world[i] # 뺀만큼 답 더해짐

# 반복문 다 돌면서 모은 ans 값 = 고이는 빗물의 총량
print(ans)
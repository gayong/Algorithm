#제로 정수 0인 경우 최근에 쓴 수 지우고, 아니면 해당 수 씀
#최종적으로 적어 낸 수의 합 출력
import sys
input = sys.stdin.readline

K = int(input())
stack = []
for k in range(K):
    n = int(input())
    if n != 0:
        stack.append(n)
    else:
        stack.pop()
print(sum(stack))

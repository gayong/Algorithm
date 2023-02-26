#곱셈 A를 B번 곱한 뒤 C로 나눈 나머지 구하기
import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

#시간초과가 바아로 떠버리네. ..
A, B, C = map(int, input().split())
# print(A ** B % C)

#분할정복
def cal(a, b):
    if b == 1:
        return a % C

    temp = cal(a, b // 2)
    if b % 2: #홀수면
        return temp * temp * a % C #절반으로 나눠서 계산 ex)2^11 = 2^5 * 2^5 * 2
    else: #짝수면
        return temp * temp % C #ex) 2^10 = 2^5 * 2^5

print(cal(A, B))

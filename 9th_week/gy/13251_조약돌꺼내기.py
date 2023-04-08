import sys
sys.stdin = open('input.txt')

def multi(n, k): #조합
    result = n
    for i in range(k - 1):
        result = result * (n - 1)
        n = n - 1
    return result

M = int(input())  #조약돌 색상 수

a = input().split()  #색상 별 조약돌 개수

list = []
for i in a:
    list.append(int(i))

K = int(input())  #뽑을 조약돌 수

N = sum(list)  #전체 돌 수
numerator = 0  #분자
denominator = multi(N, K)  #분모

#뽑을 값보다 적은 조약돌의 개수를 가진 색상은 필요없음
#해당 색상의 조약돌 제거
for i in list:
    if (i < K):
        list.remove(i)

for i in list:
    numerator += multi(i, K)

print(numerator / denominator)
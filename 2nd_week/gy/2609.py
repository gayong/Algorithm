#최대공약수와 최소공배수
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

for num in range(1, 10000):
    if a % num == 0 and b % num == 0:   #둘 다 나눠서 나머지가 0이라면
        GCD = num                       #그게 최대공약수

LCM = GCD * (a//GCD) * (b//GCD)

print(GCD, LCM, sep='\n')

#단어정렬
import sys
input = sys.stdin.readline

T = int(input())

a = []
for i in range(T):
    a += input().split()

b = list(set(a))

b.sort(key=lambda x: (len(x), x))

for word in b:
    print(word)

#나이순
import sys
input = sys.stdin.readline

T = int(input())

ppl_list = []
for i in range(T):
    ppl_list.append(input().split())

ppl_list.sort(key = lambda x :(int(x[0]), i))

for lst in ppl_list:
    print(' '.join(lst))

#생일
import sys
input = sys.stdin.readline

T = int(input())

blist = []
for i in range(T):
    blist.append(input().split())

blist.sort(key = lambda x :(int(x[3]), int(x[2]), int(x[1])))
print(blist[-1][0])
print(blist[0][0])

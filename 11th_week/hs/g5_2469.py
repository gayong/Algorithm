import sys
input = sys.stdin.readline

k = int(input())
n = int(input())
back = list(input().rstrip())
front = sorted(back)
arr = [list(input().rstrip()) for _ in range(n)]
arrFront = []
arrBack = []
length = len(arr)
for i in range(length):
    if arr[i][0] == '?':
        arrFront = arr[:i]
        arrBack = arr[i+1:]
        break

for line in arrFront:
    for i in range(k-1):
        if line[i] == "-":
            front[i], front[i+1] = front[i+1], front[i]

arrBack.reverse()
for line in arrBack:
    for i in range(k-1):
        if line[i] == "-":
            back[i], back[i+1] = back[i+1], back[i]

result = []
for i in range(len(front)-1):
    if front[i]==back[i]:
        result.append("*")
    else:
        if front[i]==back[i+1]:
            result.append("-")
        elif i!=0 and front[i]==back[i-1]:
            result.append("*")
        else:
            result = ['x' for _ in range(k-1)]
            break

print(''.join(result))
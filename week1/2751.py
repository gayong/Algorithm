#수 정렬하기
import sys
input = sys.stdin.readline
#sys.stdin.read

T = int(input().rstrip())

# a = []
# for i in range(T):
    # a.append(int(input().rstrip()))
a = [input() for i in range(T)]


a.sort()
# for num in a:
#     print(num)
sys.stdout.write('\n'.join(map(str, a)))
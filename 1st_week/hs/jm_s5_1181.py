import sys
input = sys.stdin.readline

N = int(input().rstrip())
# words = [input().rstrip() for _ in range(N)]
# words = list(set(words))
words = sorted(list(set(map(str, sys.stdin.read().split()))))
words.sort()
words.sort(key=len)


# for i in words :
#     print(i)
sys.stdout.write('\n'.join(map(str, words)))



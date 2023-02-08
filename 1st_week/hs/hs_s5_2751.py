import sys
input = sys.stdin.readline

N = int(input().rstrip())
numbers = sorted(list(map(int, sys.stdin.read().split())))

sys.stdout.write('\n'.join(map(str, numbers)))

# N = int(input().rstrip())
# numbers = []

# for i in range(N) :
#     numbers.append(int(input().rstrip()))

# numbers.sort()

# for i in range(N) :
#     print(numbers[i])

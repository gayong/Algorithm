import sys
input = sys.stdin.readline


def prime_num(N):
    numbers = list(map(int, input().split()))
    cnt = 0
    for number in numbers:
        if number == 1:
            continue
        if number == 2:
            cnt += 1
            continue
        prime = True
        for i in range(2, number):
            if number % i == 0:
                prime = False
        if prime == True:
            cnt += 1
    return cnt


if __name__ == "__main__":
    print(prime_num(input().rstrip()))

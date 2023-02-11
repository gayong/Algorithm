#피보나치
def fib(n):
    now, next = 0, 1
    for _ in range(n):
        now, next = next, now + next
    return now

N = int(input())
print(fib(N))

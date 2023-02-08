import sys
input = sys.stdin.readline

def stone(N):
    if N % 2 :
        return 'SK'
    else :
        return 'CY'

if __name__ == "__main__":
    print(stone(int(input().rstrip())))
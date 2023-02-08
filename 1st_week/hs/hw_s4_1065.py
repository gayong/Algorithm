import sys
input = sys.stdin.readline

def hansoo(n) : 
    num = str(n)
    length = len(num)
    count = 99
    if length == 1 or length == 2 :
        count = n
        return count
    for i in range(100, n+1) :
        i = str(i)
        if (int(i[0]) - int(i[1])) == (int(i[1]) - int(i[2])) :
            count += 1
    return count

if __name__ == "__main__":
    print(hansoo(int(input().rstrip())))

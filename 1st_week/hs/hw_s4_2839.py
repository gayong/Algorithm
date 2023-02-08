import sys
input = sys.stdin.readline


def sugar_deli(kg):
    if kg % 5 == 0:
        return (kg//5)
    else:
        for i in range(1, (kg//3)+1):
            f_kg = kg
            f_kg -= (3*i)
            if f_kg % 5 == 0:
                return (i+(f_kg//5))
        return -1


if __name__ == "__main__":
    print(sugar_deli(int(input().rstrip())))

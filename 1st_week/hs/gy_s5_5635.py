import sys
input = sys.stdin.readline

T = int(input().rstrip())
birth_list = []

for i in range(T):
    birth_list.append(list(map(str, input().split())))
    birth_list[i][1], birth_list[i][2], birth_list[i][3] = int(
        birth_list[i][1]), int(birth_list[i][2]), int(birth_list[i][3])

for i in range(T-1):
    if birth_list[i][3] > birth_list[i+1][3]:
        birth_list[i], birth_list[i+1] = birth_list[i+1], birth_list[i]
    elif birth_list[i][3] == birth_list[i+1][3]:
        if birth_list[i][2] > birth_list[i+1][2]:
            birth_list[i], birth_list[i+1] = birth_list[i+1], birth_list[i]
        elif birth_list[i][2] == birth_list[i+1][2]:
            if birth_list[i][1] > birth_list[i+1][1]:
                birth_list[i], birth_list[i +
                                          1] = birth_list[i+1], birth_list[i]
print(birth_list[-1][0])

for i in range(T-1):
    if birth_list[-i-1][3] < birth_list[-i-2][3]:
        birth_list[-i-1], birth_list[-i-2] = birth_list[-i-2], birth_list[-i-1]
    elif birth_list[-i-1][3] == birth_list[-i-2][3]:
        if birth_list[-i-1][2] < birth_list[-i-2][2]:
            birth_list[-i-1], birth_list[-i -
                                         2] = birth_list[-i-2], birth_list[-i-1]
        elif birth_list[-i-1][2] == birth_list[-i-2][2]:
            if birth_list[-i-1][1] < birth_list[-i-2][1]:
                birth_list[-i-1], birth_list[-i -
                                             2] = birth_list[-i-2], birth_list[-i-1]
print(birth_list[0][0])

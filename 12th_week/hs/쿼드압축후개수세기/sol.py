answer = [0,0]

def cal(arr):
    global answer
    length = len(arr)
    if length == 1:
        answer[arr[0][0]] += 1
        return
    zero = 0
    one = 0
    for i in arr:
        zero += i.count(0)
        one += i.count(1)
    if zero == length*length:
        answer[0] += 1
        return
    elif one == length*length:
        answer[1] += 1
        return
    half = length//2
    new_arr1 = [[0] * half for _ in range(half)]
    new_arr2 = [[0] * half for _ in range(half)]
    new_arr3 = [[0] * half for _ in range(half)]
    new_arr4 = [[0] * half for _ in range(half)]
    for i in range(half):
        for j in range(half):
            new_arr1[i][j] = arr[i][j]
            new_arr2[i][j] = arr[i+half][j]
            new_arr3[i][j] = arr[i][j+half]
            new_arr4[i][j] = arr[i+half][j+half]
    cal(new_arr1)
    cal(new_arr2)
    cal(new_arr3)
    cal(new_arr4)

def solution(arr):
    cal(arr)
    return answer
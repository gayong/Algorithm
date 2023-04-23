# 리턴값을 리스트로 받음
# 분할 후 구역 합칠 때 zip 이용해서 0과 1의 개수 구함

def check(x, y, n, arr):
    if n == 1:
        if arr[x][y] == 1:
            return [0, 1]
        else:
            return [1, 0]

    left_up = check(x, y, n // 2, arr)
    right_up = check(x, y + n // 2, n // 2, arr)
    left_down = check(x + n // 2, y, n // 2, arr)
    right_down = check(x + n // 2, y + n // 2, n // 2, arr)

    ################ 임포트 ##############
    # 사분면 4개가 전부 동일한 값인 경우 -> 4개 아닌 1개로 취급
    if left_up == right_up == left_down == right_down == [0, 1] or left_up == right_up == left_down == right_down == [1,0]:
        return left_up
    else:
        # 사분면 4개의 리스트 값을 idx별로 합한 결과 리턴
        return list(map(sum, zip(left_up, right_up, left_down, right_down)))


def solution(arr):
    answer = check(0, 0, len(arr), arr)

    return answer
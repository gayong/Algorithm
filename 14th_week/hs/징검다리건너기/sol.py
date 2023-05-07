def solution(stones, k):
    answer = 0
    s, e = 1, max(stones)
    while s <= e:
        m = (s + e)//2

        max_cnt = 0
        cnt = 0
        flag = False
        for stone in stones:
            if stone - m <= 0:
                if flag:
                    cnt += 1
                else:
                    max_cnt = max(max_cnt, cnt)
                    cnt = 1
                    flag = True
            else:
                flag = False

        max_cnt = max(max_cnt, cnt)

        if max_cnt >= k:
            e = m - 1
            answer = m
        else:
            s = m + 1

    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))

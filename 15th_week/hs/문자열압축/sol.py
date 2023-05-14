def solution(s):
    result = []
    if len(s) == 1:
        return 1
    for i in range(1, (len(s)//2)+1):
        b = 0
        cnt = 1
        tmp = s[:i]

        for j in range(i, len(s), i):
            if tmp == s[j:i+j]:
                cnt += 1
            else:
                if cnt != 1:
                    b += (len(str(cnt))+len(tmp))
                else:
                    b += len(tmp)
                tmp = s[j:j+i]
                cnt = 1
        if cnt != 1:
            b += (len(str(cnt))+len(tmp))
        else:
            b += len(tmp)

        result.append(b)
    return min(result)


print(solution("ababcdcdababcdcd"))

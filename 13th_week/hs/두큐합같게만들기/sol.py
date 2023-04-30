def solution(queue1, queue2):
    answer = -1
    left = sum(queue1)
    right = sum(queue2)
    target = (left+right)//2
    i, j, t = 0, 0, len(queue1)
    if not ((left+right) % 2):
        while i < 2*t and j < 2*t:
            if left < target:
                left += queue2[j]
                right -= queue2[j]
                queue1.append(queue2[j])
                j += 1
            elif left > target:
                left -= queue1[i]
                right += queue1[i]
                queue2.append(queue1[i])
                i += 1
            else:
                answer = i + j
                break
        
    return answer

print(solution([1,4], [4,8]))
from collections import Counter
def solution(gems):
    answer = []
    setGem = len(set(gems))
    gemList = Counter()
    i = 0

    for j in range(len(gems)):
        gemList[gems[j]] += 1

        while len(gemList) == setGem:
            answer.append((i + 1, j + 1))
            gemList[gems[i]] -= 1

            if not gemList[gems[i]]:
                del gemList[gems[i]]

            i += 1

    return sorted(answer, key=lambda x: (x[1] - x[0]))[0]

# def solution(gems):
#     setGems = list(set(gems))
#     length = len(gems)
#     target = len(setGems)
#     if length == target:
#         return [1, target]
#     elif target == 1:
#         return [1, 1]
#     else:
#         result = []
#         for i in range(0, length-target+1):
#             answer = [gems[i]]
#             for j in range(i, length):
#                 if gems[j] in answer:
#                     continue
#                 answer.append(gems[j])
#                 if len(answer) == target:
#                     if (j-i+1) == target:
#                         return [i+1, j+1]
#                     result.append((i+1,j+1))
#                     break
#         value = length+1
#         for i in result:
#             if (i[1]-i[0]) < value:
#                 value = i[1]-i[0]
#                 total = [i[0], i[1]]
#         return total




print(solution(["XYZ", "XYZ", "XYZ"]))


'''
(yellow의 가로 길이 * 2 + yellow의 세로 길이 * 2 + 4 = brown 넓이)
'''

def solution(brown, yellow):
    ans = []
    yellow_x = 0
    yellow_y = 0
    
    for i in range(1, yellow + 1):
        if yellow % i == 0: # 노랑의 약수
            yellow_x = int(yellow//i)
            yellow_y = i
            
            if yellow_x * 2 + yellow_y * 2 + 4 == brown:
                ans.append(yellow_x + 2)
                ans.append(yellow_y + 2)
                break
            
    return ans
dx = [0, 1, -1]
dy = [1, -1, 0]

def solution(n):
    answer = []
    if n == 1:
        answer.append(1)
    elif n == 2:
        answer = [1,2,3]
    else:
        arr = [[0]*n for _ in range(n)]
        arr[0][0] = 1
        stack = []
        stack.append((0,0,0))
        num = 2
        while stack:
            x, y, d = stack.pop()
            nx = x + dx[d]
            ny = y + dy[d]
            if nx == n or ny == n:
                stack.append((x,y,(d+1)%3))
                continue
            if not arr[ny][nx]:
                arr[ny][nx] = num
                num += 1
                stack.append((nx,ny,d))
            else:
                if not arr[y+dy[(d+1)%3]][x+dx[(d+1)%3]]:
                    stack.append((x,y,(d+1)%3))
        
        for i in range(n):
            a = i
            b = 0
            while a >= 0:
                answer.append(arr[a][b])
                a -= 1
                b += 1

    return answer

print(solution(2))
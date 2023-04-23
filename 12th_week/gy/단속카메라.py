import sys
sys.stdin = open('0input.txt')

def solution(routes):
    ans = 1
    routes.sort(key=lambda x: x[1]) # 일단 진출시점 기준으로 정렬해

    now = routes[0][1] # 첫 진출시점 now
    for route in routes:
        if now < route[0]: # 어차피 첫 루트의 진입시점은 진출시점보다 작으니 pass
            # 그 담 루트 진입시점과 첫 루트 진출시점 비교
            now = route[1] # 첫 루트의 진출시점으로 now 갱신, 그 담 루트들 진입시점이랑 계속 비교
            ans += 1
        # else:
        #     now = min(route[1], routes[i+1][0])
    return ans
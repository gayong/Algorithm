from itertools import combinations

# 각 손님들이 주문할 때, 가장 많이 함께 주문한 단품 메뉴를 코스 요리 메뉴로 구성
# 코스 요리 : 최소 2 가지 단품 + 최소 2 명의 손님이 주문했던 제품 만 포함
# 최종 -> 사전 순의 오름차순으로 정렬

def solution(orders, course):
    # 메뉴 저장
    set_menu = {}
    # n개의 조합 확인
    for i in course:
        # 각 주문 별 확인
        for order in orders:
            for comb in combinations(order, i):
                comb = sorted(comb)
                comb = "".join(comb)
                if comb not in set_menu:
                    set_menu[comb] = 0
                set_menu[comb] += 1
    # 개수 1개 이하로 주문된 세트는 제외
    set_menu = {foods: cnt for foods, cnt in set_menu.items() if cnt > 1}
    # 최대 개수 파악 위해, 코스 길이 순으로 정렬
    set_menu = sorted(set_menu.items(), key=lambda x: (len(x[0]), -x[1]))
    # 최대 개수 저장
    len_menu_cnt = dict(zip(course, [-1] * len(course)))
    # 최대 개수 메뉴만 골라내기
    answer = []
    for foods, cnt in set_menu:
        # 해당 코스에서 최대인 경우만 저장
        if len_menu_cnt[len(foods)] <= cnt:
            len_menu_cnt[len(foods)] = cnt
            answer.append(foods)
    return sorted(answer)
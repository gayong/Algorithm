from itertools import permutations

# 순열 후 순서만 바뀐 케이스 같은 케이스로 처리해야 함

# 글자 하나씩 읽으면서 유저 아이디 == 불량 아이디 확인
def isMatchId(ban_id, user_id):
    for i in range(len(ban_id)):
        if ban_id[i] == '*':
            continue
        elif ban_id[i] != user_id[i]:
            return False
    return True

# 유저 아이디의 길이와 불리 사용자 아이디의 길이가 다르면 거르기
# 각각 아이디 일치하는지 isMatchId에서 확인
def check_len(banned_ids, candidate_users):
    for i in range(len(banned_ids)):
        if len(banned_ids[i]) != len(candidate_users[i]):
            return False
        if isMatchId(banned_ids[i], candidate_users[i]) is False:
            return False
    return True


def solution(user_ids, banned_ids):
    ans = list()

    # 블리 길이만큼 모든 조합의 수 만들기
    for candidate_users in permutations(user_ids, len(banned_ids)):
        # 유저랑 블리 아이디 매치되는지 확인
        if check_len(banned_ids, candidate_users) is True:
            # 순서만 다른 조합 거르기 위한 set
            candidate_users = set(candidate_users)
            if candidate_users not in ans:
                ans.append(candidate_users)

    return len(ans)
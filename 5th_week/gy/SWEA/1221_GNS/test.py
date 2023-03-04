import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)] # 문단 받아오기

    for i in range(N): # 가로회문 비교
        for l in range(N-M+1):
            word_list = []
            cnt = 0
            for j in range(l,l+M):
                word_list.append(arr[i][j]) # arr의 i행 j열 비교하면서 한 문장씩 받아오기
                new_word_list = word_list[:] # 받아온 리스트를 새 리스트로 받음
                new_word_list.reverse()
            for k in range(len(word_list)):
                if word_list[k] == new_word_list[k]: # 원래 리스트와 새 리스트의 모양 비교
                    cnt += 1 # 모양이 같을 경우 카운트
            if cnt == M: # 길이가 M인 회문이므로 카운트와 M이 같을 경우 리스트 반환
                print(f'#{tc}', ''.join(word_list))

    # 전치행렬로 바꾸기
    for i in range(N):
        for j in range(N):
            if i<j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for i in range(N): # 세로 회문 비교
        for l in range(N - M + 1):
            word_list = []
            cnt = 0
            for j in range(l,l + M):
                word_list.append(arr[i][j])

                new_word_list = word_list[:]
                new_word_list.reverse()
            for k in range(len(word_list)):
                if word_list[k] == new_word_list[k]:
                    cnt += 1
            if cnt == M:
                 print(f'#{tc}', ''.join(word_list))
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) #길이 K인 단어 몇개 들어가나
    pz = [list(map(int, input().split())) for _ in range(N)]
    print(pz)



#list(zip(*행렬))

#row에서 띄어쓰기 없애고 0으로 split하면 1로된 리스트 나오는데 그중에서 연속으로 k개 있는 요소들을 세면 됩니다.
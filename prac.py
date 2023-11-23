import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    l = list(map(int, input().split()))
    # A, B, C, D = map(int, input().rstrip().split())
print(l)
#------------------------------------------
# 이러면 중첩리스트로 안들어감;; append 쓰면 리스트 속 리스트 됨
T = int(input())

a = []
for i in range(T):
    a += input().split()
#------------------------------------------
#리스트 안에 든거 그냥 한줄씩 빼오기
for word in b:
    print(word)
#------------------------------------------
# T = int(input())
# for test_case in range(1, T+1):
#     num = list(map(int,input().split()))
#     avg = sum(num)/len(num)
#     avg = round(avg)
#     print("#{} {}".format(test_case, avg))
# #------------------------------------------
# num = int(input())
# #print(T)
# for i in range(num):
#     l = list(map(int,input().split()))
#     l.sort()
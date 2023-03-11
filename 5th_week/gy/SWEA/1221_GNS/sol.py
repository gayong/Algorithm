import sys
sys.stdin = open('GNS_test_input.txt')

dicts = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6,
             'SVN':7, 'EGT':8, 'NIN':9}
dicts_k = {0:'ZRO', 1:'ONE', 2:'TWO', 3:'THR', 4:'FOR', 5:'FIV', 6:'SIX',
             7:'SVN', 8:'EGT', 9:'NIN'}
T = int(input())
for tc in range(1, T+1):
    i, tc_num = map(str, input().split())
    arr = list(map(str, input().split()))
    num_lst = [dicts[char] for char in arr]
    num_lst.sort()
    result_lst = [dicts_k[num] for num in num_lst]

    print(i)
    print(*result_lst)
#################################
T = int(input())
for tc in range(T):
    num, N = input().split()

    numbers = list(input().split())

    naemamdaero = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    numbers.sort(key=lambda x: naemamdaero.index(x))

    print(num)
    print(*numbers)
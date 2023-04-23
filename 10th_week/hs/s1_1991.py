import sys
input = sys.stdin.readline

def order(node):
    if node != '.':
        pre_list.append(node)
        order(tree[node][0])
        in_list.append(node)
        order(tree[node][1])
        post_list.append(node)

N = int(input())
tree = dict()

for i in range(N):
    lst = input().split()
    tree[lst[0]] = lst[1], lst[2]
    
pre_list = []
in_list = []
post_list = []

order('A')
print(''.join(pre_list))
print(''.join(in_list))
print(''.join(post_list))

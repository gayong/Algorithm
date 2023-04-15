import sys
sys.stdin = open('input.txt')

def preorder(node):
    print(node, end='')
    #왼쪽 자식을 조사
    if tree[node][0] != None:
        preorder(tree[node][0])
    #오른쪽 자식 조사
    if tree[node][1] != None:
        preorder(tree[node][1])

def inorder(node):
    # 왼쪽 자식을 조사
    if tree[node][0] != None:
        inorder(tree[node][0])
    print(node, end='')
    #오른쪽 자식 조사
    if tree[node][1] != None:
        inorder(tree[node][1])

def postorder(node):
    # 왼쪽 자식을 조사
    if tree[node][0] != None:
        postorder(tree[node][0])
    # 오른쪽 자식 조사
    if tree[node][1] != None:
        postorder(tree[node][1])
    print(node, end='')

V = int(input())    #노드의 개수
tree = {} #딕셔너리 형태로 넣음
for i in range(V):
    p, l, r = map(str, input().split())
    if l == '.':
        l = None
    if r == '.':
        r = None
    tree[p] = l, r

# print(tree)

preorder('A')
print()
inorder('A')
print()
postorder('A')

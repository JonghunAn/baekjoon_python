import sys
 
N=int(sys.stdin.readline())
#이진트리
tree=[[] for _ in range(N+1)]
for _ in range(N):
    s=list(map(str,sys.stdin.readline().split()))
    c=ord(s[0])-64
    for i in range(1,3):
        tree[c].append(ord(s[i])-64)
 
def pre_order(start):
    print(chr(start + 64), end="")
    if tree[start][0] != -18:
        pre_order(tree[start][0])

    if tree[start][1] != -18:
        pre_order(tree[start][1])
 
def in_order(start):
    if tree[start][0]!=-18:
        in_order(tree[start][0])
    print(chr(start+64),end="")
    if tree[start][1]!=-18:
        in_order(tree[start][1])
 
def post_order(start):
    if tree[start][0]!=-18:
        post_order(tree[start][0])
 
    if tree[start][1]!=-18:
        post_order(tree[start][1])
    print(chr(start + 64), end="")
 
 
pre_order(1)
print()
in_order(1)
print()
post_order(1)

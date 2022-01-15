import sys
sys.setrecursionlimit(10 ** 9)
pre_order=[]

while True:
    try:
       pre_order.append(int(sys.stdin.readline())) 
    except:
        break

def post_order(start, end):
    if start > end:
        return

    root = pre_order[start]
    pivot = end + 1
    for i in range(start+1, end+1):
        if root < pre_order[i]:
            pivot = i
            break
    post_order(start+1, pivot - 1)
    post_order(pivot, end)
    print(root)
    
if pre_order:
    post_order(0, len(pre_order) - 1)
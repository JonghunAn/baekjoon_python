a,b = map(int,input().split())
g=[list(map(int,input().split())) for _ in range(b)]

def bfs(g,a,b,target):
    move = [(-1,0),(1,0),(0,-1),(0,1)]
    targets = target
    nexts = []
    n = len(targets)
    for _ in range(n):
        i,j = targets.pop()
        for p,q in move:
            if 0<=i+q<b and 0<=j+p<a:
                if g[i+q][j+p]==0:
                    g[i+q][j+p]=1
                    nexts.append((i+q,j+p))
    return nexts

answer = 0
tmp = [(i,j) for i in range(b) for j in range(a) if g[i][j]==1]
while True:
    tmp = bfs(g,a,b,tmp)
    if not tmp:
        break
    answer +=1
for x in g:
    if 0 in x:
        answer = -1
        break
print(answer)
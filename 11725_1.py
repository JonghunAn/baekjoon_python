import sys
sys.setrecursionlimit(10**6)

num = int(sys.stdin.readline())
visit = list(0 for i in range(num+1))
nodes=[[] for _ in range(num+1)]
parent=[0 for _ in range(num+1)]

for i in range(num-1):
    v1,v2 = map(int,sys.stdin.readline().split())
    nodes[v1].append(v2)
    nodes[v2].append(v1)
print(nodes)
def dfs(num):
        visit[num] = 1
        for child in nodes[num]:
            if visit[child] ==0:
                parent[child] = num
                dfs(child)
        
dfs(1)
print(*parent[2:],sep="\n")

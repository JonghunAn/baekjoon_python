import sys

computers = int(sys.stdin.readline())
vertex_num = int(sys.stdin.readline())
link = [[] for _ in range(computers+1)]
visit = [0 for _ in range(computers+1)]
count =0
for _ in range(vertex_num):
    v1,v2 = map(int,sys.stdin.readline().split())
    link[v1].append(v2)
    link[v2].append(v1)

def dfs(v):
    global count
    if(visit[v]==0):
        visit[v] = 1
        count+=1
        for new_v in link[v]:
            dfs(new_v)
    return count

print(dfs(1)-1)
import sys
candidate = [(2,1),(1,2),(2,-1),(1,-2),(-1,2),(-1,-2),(-2,1),(-2,-1)]

def bfs(able,visited):
    global count
    if(eX,eY) in able:
        print(count)
    else:
        count+=1
        temp=[]
        for a in able:
            for c in candidate:
                nx,ny = a[0]+c[0], a[1]+c[1]
                if 0<=nx<l and 0<=ny<l and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    temp.append((nx,ny))
        bfs(temp,visited)

N=int(input())
for _ in range(N):
    l = int(input())
    sX,sY = map(int,input().split())
    eX,eY = map(int,input().split())
    visited = [[0 for _ in range(l)] for _ in range(l)]
    count=0
    able = [(sX,sY)]
    visited[sX][sY]=1
    bfs(able,visited)
        
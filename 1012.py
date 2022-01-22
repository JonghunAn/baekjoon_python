import sys
sys.setrecursionlimit(10000)
test_case = int(sys.stdin.readline())
result = []

def bfs(x1,y1,location,visit,x,y):
    global count
    if(visit[x1][y1]==0):
        count+=1
        visit[x1][y1]=1
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for idx in range(4):
            new_x = x1+dx[idx]
            new_y = y1+dy[idx]
            if not(0<=new_x<=x):
                continue
            elif not (0<=new_y<=y):
                continue
            else:
                if(location[new_x][new_y] ==1):
                    if(visit[new_x][new_y]==0):
                        visit[new_x][new_y]=1
                        bfs(new_x,new_y,location,visit,x,y)
                        

for _ in range(test_case):
    x,y,num = map(int,sys.stdin.readline().split())
    location = [[0 for _ in range(y+1)] for _ in range(x+1) ]
    visit = [[0 for _ in range(y+1)] for _ in range(x+1) ]
    count=0
    start=0
    x1=0
    y1=0
    for i in range(num):
        v1,v2 = map(int,sys.stdin.readline().split())
        location[v1][v2] = 1

    for x1 in range(x+1):
        for y1 in range(y+1):
                if(location[x1][y1]==1):
                    bfs(x1,y1,location,visit,x,y)
    print(count)

    
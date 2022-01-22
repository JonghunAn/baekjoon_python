import sys

def bfs(able,visit):
    global result
    if (t_x,t_y) in able:
        print(result)
    else:
        result+=1    
        temp=[]
        dx = [-1, 1, 2, 2, 1, -1, -2, -2]
        dy = [2, 2, 1, -1, -2, -2, -1, 1]
        for a in able:
            for i in range(8):
                new_x = a[0]+dx[i]
                new_y = a[1]+dy[i]
                if(0<=new_x<l and 0<=new_y<l and visit[new_x][new_y]==0):
                    visit[new_x][new_y]=1
                    temp.append((new_x,new_y))
        bfs(temp,visit)       
    
test_case =int(sys.stdin.readline())
for _ in range(test_case):
    result = 0
    l = int(sys.stdin.readline())
    visit = [[0 for _ in range(l)] for _ in range(l)]
    x,y = map(int,sys.stdin.readline().split())
    t_x,t_y = map(int,sys.stdin.readline().split())
    able=[(x,y)]
    visit[x][y]=1
    bfs(able,visit)

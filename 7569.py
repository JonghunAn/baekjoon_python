import sys
from collections import deque

def BFS():
    while queue:
        x,y,z = queue.popleft()

        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if matrix[nx][ny][nz] == 0:
                    matrix[nx][ny][nz] = matrix[x][y][z] + 1
                    queue.append((nx,ny,nz))


m,n,h = map(int,input().split())
matrix = [[] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        matrix[i].append(list(map(int, input().split())))

dx = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]
dz = [1,-1,0,0,0,0]                            
 
is_fine=True    #이미 다 익었는지 확인
result=0
queue = deque()
                   
for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 1:
                queue.append((i,j,k))
            elif matrix[i][j][k]==0:
                #안익은 토마토가 있는경우
                is_fine = False
        
                
BFS()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if(matrix[i][j][k] ==0):
                print(-1)
                sys.exit(0)
            result = max(result,matrix[i][j][k])
            
            
if is_fine==True:
           print(0)
else:
    print(result)         

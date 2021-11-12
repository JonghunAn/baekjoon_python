from collections import deque
import sys

n,m = map(int,input().split())
matrix=[]
for i in range(n):
        line = sys.stdin.readline().rstrip('\n')
        matrix.append(list(map(int,line)))
        
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
            x,y = queue.popleft()
            
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                
                if 0<=nx<n and 0<=ny<m:
                    #범위설정 
                    if matrix[nx][ny] == 1:
                        matrix[nx][ny] = matrix[x][y]+1
                        queue.append((nx,ny))   #경로 수 추가
    return matrix[n-1][m-1]

print(BFS(0,0))

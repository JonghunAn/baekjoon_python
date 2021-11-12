import sys
N = int(sys.stdin.readline())
arr = []
visited = [[0]*N for _ in range(N)]

for i in range(N):
    arr.append(list(map(int,sys.stdin.readline().rstrip('\n'))))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
#방향확인

def DFS(x,y):
    visited[x][y] = 1
    global check_num
    if arr[x][y] ==1:
        check_num+=1
    for i in range(4):
        nx = x +dx[i]
        ny = y +dy[i]
        if 0<= nx < N and 0 <= ny < N:
            #범위 설정
            if visited[nx][ny] ==0 and arr[nx][ny] ==1:
                DFS(nx,ny)
                
check_num = 0  #단지 수
check_num_list = []

for i in range(N):
    for j in range(N):
        if arr[i][j] ==1 and visited[i][j] ==0:
            DFS(i,j);
            check_num_list.append(check_num)
            check_num=0
            
print(len(check_num_list))  #단지수 출력
for val in sorted(check_num_list):
    print(val) #단지 내 집의 수
N,M,V = map(int,input().split(" "))
start = V
graph = []
visited = [0 for i in range(N) ];
connect = [0 for i in range(M)]

stack = []
DFS_res = []

queue = []
BFS_res =[]

for i in range(M):
    x,y = map(int,input().split())
    graph.append([x,y]);


def DFS_search(V,graph,Min) :
    for i in range(M):   
            if V == graph[i][0]:
                if(Min>=graph[i][1] and connect[i]==0 and visited[graph[i][1]-1] ==0):
                    Min = graph[i][1]
                    connect[i]=1
            elif V == graph[i][1]:
                if(Min>=graph[i][0] and connect[i]==0 and visited[graph[i][0]-1] ==0):
                    Min = graph[i][0]
                    connect[i]=1
    return Min
    #최소번호값 리턴 
    
#1. DFS
while(True):
    Min = N+1
    
    if(V != Min):        
        #이어진 연결 선이 있는경우
            stack.append(V)
            #스택추가
            DFS_res.append(V)
            #결과에 추가
            visited[V-1] = 1
            #방문정보 저장
            
            V=DFS_search(V,graph,Min)
    else:
           #이어진 연결 선이 없는경우
           V = stack.pop()
           V=DFS_search(V,graph,Min)
           
           if(len(stack)==0):
                for v in range(N):
                     if(visited[v]==0):
                        #  DFS_res.append(v+1)
                        # 연결선이 없는것도 처리할 경우 추가
                          #배열 0부터 시작 +1 
                          visited[v]=1
                   
    
    if all(visited)==True:
        for vertex in DFS_res:
            print(vertex, end=" ")
        print()
        break
            #모든 노드 방문시 DFS 결과 출력

    
#2. BFS
def BFS_search(V,graph):
    temp = []
    for i in range(M):   
            if V == graph[i][0]:
                if(graph[i][1] not in BFS_res):
                     temp.append(graph[i][1])
                     
            elif V == graph[i][1]:
                    if(graph[i][0] not in BFS_res):
                               temp.append(graph[i][0])
    temp.sort()
    BFS_res.extend(temp)
    queue.extend(temp)
    if(len(queue)!=0):
        return queue.pop(0)
    #최소번호값 리턴 
    else:
        return -1

    
V = start
visited = [0 for i in range(N) ]
connect = [0 for i in range(M)]
#초기화 진행
BFS_res.append(V)
visited[V-1]=1

while True:
    V = BFS_search(V,graph)
    
    if V ==-1:
        for vertex in BFS_res:
            print(vertex,end=" ")
        break
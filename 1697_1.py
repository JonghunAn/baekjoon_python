n,k = map(int,input().split())

que =[]
visit= [0 for _ in range(100001)]
depth=[]

depth.append(0)
que.append(n)

while True:
    x = que.pop(0)
    xc = depth.pop(0)
    
    if visit[x] ==0:
        visit[x]=1
        
        if x-1 >=0:
            que.append(x-1)
            depth.append(xc+1)
        if 2*x <= 100000:
            que.append(2*x)
            depth.append(xc+1)
        if x+1 <= 100000:
            que.append(x+1)
            depth.append(xc+1)
    
    if x == k:
        print(xc)
        break
    
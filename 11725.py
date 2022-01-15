import sys
num = int(sys.stdin.readline())
nodes=[]
visit = list(0 for i in range(num+1))

for i in range(num-1):
    v1,v2 = map(int,sys.stdin.readline().split())
    nodes.append([v1,v2])
    nodes.append([v2,v1])
 
print(nodes)
for i in range(2,num):
    for j in range(len(nodes)):
        if(nodes[j][0] == i):
            print(nodes[j][1])
            break
            
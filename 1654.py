import sys
input = sys.stdin.readline()
k,n = map(int,input.split())
cables=[]
result=0
for i in range(k):
    cables.append(int(sys.stdin.readline()))
    
def binary_search(start,end):
    global result
    cable_num =0
    mid = (start+end)//2
    
    if(start>end):
        print(result)
        return
    #end 길이까지 탐색해야함
    
    for idx in range(k):
        cable_num+=cables[idx]//mid
        
    if(cable_num>=n):
        result=mid
        start = mid+1
        binary_search(start,end)
    elif(cable_num<n):
        end = mid-1
        binary_search(start,end)
        

start = 1
end = max(cables)
binary_search(start,end)

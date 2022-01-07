import sys
n,m = map(int,sys.stdin.readline().split())
wood_list=[]
wood_list = list(map(int,sys.stdin.readline().split()))

start=0
end=max(wood_list)

while(start<=end):
    mid = (start+end)//2
    result =0
    for wood in wood_list:
        if wood>mid:
            result+=wood-mid
        if result>=m:
            break
        
    if (result>=m):
        start = mid+1
    else:
        end = mid-1
print(end)

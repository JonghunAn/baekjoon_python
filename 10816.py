import sys

list1 =[]
list2 =[]

list1_num = int(sys.stdin.readline())
list1 = list(map(int,sys.stdin.readline().split()))
list2_num = int(sys.stdin.readline())
list2 = list(map(int,sys.stdin.readline().split()))

list1.sort()

def leftCheck(val,mid,start):
    count=0
    while mid >start:
        mid-=1
        if list1[mid]==val:
            count+=1
        else:
            break
    return count

def rightCehck(val,mid,end):
    count=0
    while mid <end:
        mid+=1
        if list1[mid]==val:
            count+=1
        else:
            break
    return count
        
for idx in range(list2_num):
    val = list2[idx]
    start = 0
    end = list1_num-1
    count = 0
    while True:
        mid = (start+end)//2
        if val == list1[mid]:
            count+=1
            count+=leftCheck(val,mid,start)
            count+=rightCehck(val,mid,end)
            print(count,end=" ")
            break
        elif list1[mid]>val:
            end=mid-1
        elif list1[mid]<val:
            start=mid+1
            
        if start>end:
            print(count,end=" ")
            break
import sys

list1 =[]
list2 =[]

list1_num = int(sys.stdin.readline())
list1 = list(map(int,sys.stdin.readline().split()))
list2_num = int(sys.stdin.readline())
list2 = list(map(int,sys.stdin.readline().split()))

list1.sort()

for idx in range(list2_num):
    val = list2[idx]
    start = 0
    end = list1_num-1
    count = 0
    while True:
        mid = (start+end)//2
        if val == list1[mid]:
            count+= list1.count(val)
            print(count,end=" ")
            break
        elif list1[mid]>val:
            end=mid-1
        elif list1[mid]<val:
            start=mid+1
            
        if start>end:
            print(count,end=" ")
            break
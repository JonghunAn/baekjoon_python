import sys
list1 = []
list2 = []
list1_num = int(sys.stdin.readline())
list1 = list(map(int,sys.stdin.readline().split()))
list2_num = int(sys.stdin.readline())
list2 = list(map(int,sys.stdin.readline().split()))

list1.sort()
start = 0
end = len(list1)-1
mid = end//2

for idx in range(list2_num):
    start=0
    end = len(list1)-1
    val = list2[idx] 
    while True:
        mid = (start+end)//2
        if val == list1[mid]:
            print(1) 
            break;
        elif list1[mid] >val :
            end = mid-1
        elif list1[mid]<val:
            start = mid+1
        
        if start>end:
            print(0)
            break;
import sys
list1 = []
list2 = []
list1_num = int(sys.stdin.readline())
list1 = list(map(int,sys.stdin.readline().split()))
list2_num = int(sys.stdin.readline())
list2 = list(map(int,sys.stdin.readline().split()))

list1.sort()
start = 0
end = len(list1)
mid = end//2

for idx in range(list2_num):
    val = list2[idx] 
    while True:
        if val == list1[mid]:
            start=0
            end = len(list1)
            mid = end//2
            print(1) 
            break;
        elif mid == end or mid == start :
            start=0
            mid = len(list1)//2
            end = len(list1)
            print(0)
            break; 
        elif list1[mid] >val :
            end = mid
            mid = end//2
        elif list1[mid]<val:
            start = mid
            mid = (start+end)//2
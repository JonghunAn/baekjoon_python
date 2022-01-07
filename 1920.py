import sys
list1 = []
list2 = []
list1_num = int(sys.stdin.readline())
list1 = list(map(int,sys.stdin.readline().split()))
list2_num = int(sys.stdin.readline())
list2 = list(map(int,sys.stdin.readline().split()))

for i in range(list2_num):
    if list2[i] in list1:
        print(1)
    else:
        print(0)
import sys
 
list1_num = int(sys.stdin.readline())
list1 = list(map(int, sys.stdin.readline().split()))
list2_num = int(sys.stdin.readline())
list2 = list(map(int, sys.stdin.readline().split()))
 
dic = dict()
 
for i in list1:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
 
for i in range(list2_num):
    if list2[i] in dic:
        print(dic[list2[i]], end=' ')
    else:
        print(0, end=' ')
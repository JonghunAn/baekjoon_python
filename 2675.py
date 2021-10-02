num = int(input())
for i in range(num):
    listNum,list = input().split()
    for j in range(len(list)):
        for k in range(int(listNum)):
            print(list[j],end="")
    print()

A = int(input())
B = int(input())
C = int(input())
result = str(A*B*C)

checkList =list(map(str,range(10)))

for i in range(len(checkList)):
    num =0
    for j in range(len(result)):
        if (result[j] == checkList[i]):
             num+=1
    print(num)
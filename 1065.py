num = int(input())
check =0
for i in range(1,num+1):
    if(i<100):
        check+=1
    else:
        j = []
        j = str(i)
        if(int(j[0])+int(j[2]) == int(j[1])*2):
            check+=1
print(check)

        
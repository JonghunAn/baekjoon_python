kg = int(input())
num=0
while True:
    if(kg<0):
        print(-1)
        break
    elif(kg%5==0):
        num+=int(kg//5)
        print(num)
        break
    else:
        kg-=3
        num+=1
        if(kg==0):
            print(num)
            break


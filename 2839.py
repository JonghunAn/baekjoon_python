kg = int(input())
num = 0

while True:
    if(kg<3):
        break
    elif(kg%5!=0):
        kg-=3
    elif(kg%3!=0):
        kg-=5
    num+=1
        

if(kg!=0):
    print(-1)
else:
    print(num)
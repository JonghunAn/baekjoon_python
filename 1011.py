import math

num_list = int(input())

for i in range(num_list):
    x,y = map(int,input().split())
    d = y-x
    temp = int(math.sqrt(d))    
    moves = (2*(temp-1)+1)
    left = d-temp**2
    while True:
        if(left==0):
            print(moves)
            break
        else:
            if(left-temp>=temp):
                left-=temp
                moves+=1
            elif(left-temp>=0):
                left-=temp
                temp-=1
                moves+=1
            else:
                temp-=1
num = int(input())
check =0
for i in range(1,10000):
   if  (i*(i+1))/2 >= num :
       check=i
       break


right = int(num- (((check-1)*check)/2))
left = check+1-right

if((check%2)==0):
    print(right,"/",left)

elif((check%2)==1):
     print(left,"/",right)
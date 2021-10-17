num = int(input())
arr = [["*"]*num for _ in range(num)]

def printStar(num):
    temp = int(num/3)
    for i  in range(temp,temp*2):
        for j in range(temp,temp*2):
            arr[i][j] =" "
        
    if(num>=9):
        printStar(int(num//3))
        print()
        
    
printStar(num)

# num = int(input())
# arr = [["*"]*num for _ in range(num)]

# def printStar(num,i,j):
#     temp_x = i//3
#     temp_y = j//3
#     for i  in range(temp_x,temp_x*2):
#         for j in range(temp_y,temp_y*2):
#             arr[i][j] =" "
#     if(temp_x>1 and temp_y>1):
#         for i in range(temp_x, num, temp_x):
#             for j in range(temp_y, num, temp_y):
#                 printStar(num,i,j)

# printStar(num,num,num)

# for i in range(num):
#             for j in range(num):
#                 print(arr[i][j], end=" ")
#             print()
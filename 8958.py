quizNum = int(input())
oxList = list(input() for i in range(quizNum))
result = []
for i in range(quizNum):
    num = 0
    sum = 0
    for j in range(len(oxList[i])):
        if(oxList[i][j] == 'O'):
            num+=1
            if(num==1):
                sum+=1
            else:
                sum+=num
        else:
            num=0
    result.append(sum)

for i in range(quizNum):
    print(result[i])
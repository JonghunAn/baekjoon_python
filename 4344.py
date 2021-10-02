import statistics
listNum = int(input())
scores = []
for i in range(listNum):
    scores = list(map(int,input().split()))
    exp = statistics.mean(scores[1:])
    num = 0
    for j in range(1,scores[0]+1):
        if(scores[j] > exp):
           num+=1

    result = num/scores[0]*100
    print("%0.3f%%" % result)

import statistics

list_num = int(input())
scores = list(map(int,input().split()))
newScores = []
maxVal = max(scores)
for i in range(len(scores)):
    scores[i] = (scores[i]/maxVal*100)

print(round(statistics.mean(scores),2))

case = int(input())
profiles = []
rank = [1 for i in range(case)]
for i in range(case):
    profile = list(map(int,input().split()))
    profiles.append(profile)

for i in range(case):
    for j in range(case):
        if(i==j):
            continue
        if(profiles[i][0] < profiles[j][0] and profiles[i][1] < profiles[j][1]):
            rank[i] +=1

for i in range(case):
    print(rank[i],end=" ")

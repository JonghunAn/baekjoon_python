import sys

count = int(input())
info = []
for i in range(count):
    age,name = sys.stdin.readline().split()
    age = int(age)
    info.append([age,name])

info.sort(key=lambda x:x[0])

for val in info:
    print(val[0],val[1],sep=" ")
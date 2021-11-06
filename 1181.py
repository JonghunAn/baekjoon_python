import sys
count = int(input())
arr=[]
for i in range(count):
    text = sys.stdin.readline()
    arr.append(text)
arr = set(arr)
arr = list(arr)
arr.sort()
arr.sort(key=len)

for i in arr:
    print(i,end="")
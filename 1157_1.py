msg = list(input().upper())
count= [0 for i in range(26)]
check=0

for i in range(26):
   count[i] = msg.count(chr(65+i))
   
for i in range(len(count)):
    max_val = max(count)
    if(max_val == count[i]):
        check+=1

if(check!=1) :
    print("?")
else:
    print(chr(65+count.index(max(count))))
    # // 최대값 index찾기
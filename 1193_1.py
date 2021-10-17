num = int(input())
count = 1

while True:
    if num > int(count*(count+1)/2):
        count = count + 1
    else:
        break

result = num - (count-1)*(count)/2

str1 = str(int(result))
str2 = str(int((count-(result-1))))
if count % 2 == 0:
    print(str1 +'/'+str2)
else:
    print(str2+'/'+str1)
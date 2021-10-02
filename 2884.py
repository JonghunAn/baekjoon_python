hour, min = map(int, input().split())

if min<45:
    if hour<=0:
        hour = 23
    else:
        hour-=1
    min = 15+min

else:
    min = min-45
print(hour,min)
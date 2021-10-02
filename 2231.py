val = int(input())

for i in range(val):
    temp = sum(map(int, str(i)))
    result = i + temp
    if result == val:
        print(i)
        break
else:
    print(0)
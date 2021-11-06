count = int(input())

array = []

for i in range(count):
    array.append(int(input()))
    array.sort()

for i in range(count):
    print(array[i])
    
value = int(input())

check = value
new =0
iter=1
while True:
    new = (value%10 + int(value/10))
    if (new<10):
        new+=((value%10)*10)
    else:
        new %=10
        new += ((value % 10) * 10)

    value = new
    if (new == check):
        break
    else:
        iter += 1

print(iter)


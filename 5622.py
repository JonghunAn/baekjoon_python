str = input()
dial = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
result = 0
for j in range(len(str)):
    for i in dial:
        if str[j] in i:
            result += dial.index(i)+3
print(result)
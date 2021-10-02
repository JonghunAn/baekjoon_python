nums = list(map(int,(input() for i in range(10))))
result =[]
check = 10
for i in range(len(nums)):
    result.append(nums[i] % 42)
    for j in range(i):
            if(result[j] == result[i]):
                check-=1
                break
print(check)



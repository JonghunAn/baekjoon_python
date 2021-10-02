num1, num2 = input().split()

num1 = int("".join(reversed(num1)))
num2 = int("".join(reversed(num2)))

print(num1) if num1>num2 else print(num2)

# num1 = int(num1[::-1])
# num2 = int(num2[::-1])
#
# if num1 > num2:
#     print(num1)
# else :
#     print(num2)

##코드리뷰
num = int(input())
result =1 

def factorial(num,result):
    if(num>=1):
        result*=num
        num-=1
        factorial(num,result)
    else:
        print(result)

factorial(num,result);
def solution(s):
    numbers = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i in range(len(numbers)):
       idx = s.find(numbers[i])
       if(idx==-1):
           continue
       else:
            s = s[:idx]+str(i)+s[idx+1:]
            s = s[:idx+1]+s[idx+len(numbers[i]):]
    return int(s)

print(solution("sevenseven"))
msg = input()

msg = msg.replace("=","0")
msg = msg.replace("-","1")
#변경된문자열 반환 참조x
croatia = ["c0","c1","dz0","d1","lj","nj","s0","z0"]
check = 0
for i in range(len(croatia)):
    if(i==2):
        check+=msg.count(croatia[i])
         #dz= 케이스 추가
    else:
         check+= msg.count(croatia[i])
         #dz= 케이스 한번더 추가
print((len(msg)-check))
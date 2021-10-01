#msg = list(sys.stdin.readline())
msg = list(input().upper())
msg_len = len(msg)
dic_list = []
dic_num = [0 for i in range(msg_len)]
for i in range(msg_len):
    char = msg[i]
    # if(char>='a' and char<='z'):
    #     msg[i] = chr(ord(char)-32)

    if char in dic_list :
        idx = dic_list.index(char)
        dic_num[idx]+=1
    else:
        dic_list.append(char)
        idx = len(dic_list)-1
        dic_num[idx]=1

check=0
for i in range(msg_len):
    max_val = max(dic_num)
    if(max_val == dic_num[i]):
        check+=1

if(check!=1) :
    print("?")
else:
    idx = dic_num.index(max(dic_num))
    # // 최대값 index찾기
    print(dic_list[idx])
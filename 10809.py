list = input()
ascii = [i for i in range(97,123)]
alphabet = [-1 for i in range(26)]
for i in range(len(list)):
    for j in range(len(alphabet)):
        if(ascii[j] == ord(list[i]) & alphabet[j] != -1):
            alphabet[j] = i
            ascii[j] = -1
            break

for i in range(len(alphabet)):
    print(alphabet[i], end=" ")

    # 코드리뷰
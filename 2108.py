import sys
count = int(input())
arr = [int(sys.stdin.readline()) for i in range(count)]
# arr_count = [0 for _ in range(count)]


print(int(round(sum(arr)/count)))   #산술평균
arr.sort()
print(arr[count//2])    #중간값

# for i  in range(count):
#     for j in range(count):
#         if arr[i] == arr[j]:
#             arr_count[i]+=1

# val = max(arr_count)
# temp =[]
# for i in range(count):
#     if arr_count[i] == val :
#         temp.append(arr[i])

# if(len(temp)==1):
#     print(temp[0]) #최빈값
# else:
#     temp.sort()
#     k=1
#     while True:
#         if(temp[0] != temp[k]):
#             print(temp[k]) #최빈값
#             break
#         else:
#             k+=1


from collections import Counter
k=Counter(arr).most_common()

if len(arr) > 1:  #만약 입력값이 하나면 , 그게 최빈값이 되므로 예외처리
    if k[0][1] == k[1][1]:
        print(k[1][0]) 
    # 최빈값의 빈도수를 비교하여, 2개이상의 최빈값이 있으면 두번째로 작은것을 출력
    else : print(k[0][0]) 
else : print(arr[0]) 


print(max(arr)-min(arr))  #범위
# import sys

# def quickSort(arr):
#     if len(arr)<=1 :
#         return arr
#     pivot = arr[len(arr)//2]
#     left_arr, equal_arr, right_arr = [],[],[]
#     for i in arr:
#         if i < pivot : 
#             left_arr.append(i)
#         elif i > pivot : 
#             right_arr.append(i)
#         else : equal_arr.append(i)
#     return quickSort(left_arr)+equal_arr+quickSort(right_arr)


# count = int(sys.stdin.readline())
# array = list(int(sys.stdin.readline()) for _ in range(count))
# array = quickSort(array)

# for i in range(count):
#     print(array[i])


import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)

# def quickSort(array,start,end):
#     if (start>=end):
#         return
#     pivot = start
#     left = start+1
#     right = end
#     while(left<=right):
#         while(left<=end and array[left]<=array[pivot]):
#             left+=1
#         while(right>start and array[right]>=array[pivot]):
#             right-=1
#         if(left>right):
#             array[right],array[pivot] = array[pivot],array[right]
#         else:
#             array[left],array[right] = array[right],array[pivot]
        
#         quickSort(array,start,right-1)
#         quickSort(array,right+1,end)
#     return array


def mergeSort(array):
    if len(array)<=1:
        return array
    mid = len(array)//2

    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    result = []
    i,j,k = 0,0,0

    while i < len(left) and j <len(right):
        if(left[i]<right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    result += left[i:]
    result += right[j:]

    return result


import sys

count = int(sys.stdin.readline())
array = list(int(sys.stdin.readline()) for _ in range(count))
# array.sort()
array = mergeSort(array)

for i in range(count):
    print(array[i])


list1_num= int(input())
list1 = list(map(int, input().split()))
list2_num = int(input())
list2 = list(map(int, input().split()))
d = []
list1.sort()

def upper_bound(start, end, val):
    while(end - start > 0):
        mid = (start+end)//2
        if(list1[mid] <= val):
            start = mid+1
        else:
            end = mid
    return end+1
    
def lower_bound(start, end, val):
    while(end - start > 0):
        mid = (start+end)//2
        if(list1[mid] < val):
            start = mid+1
        else:
            end = mid
    return end+1
    
for val in list2:
    d.append(upper_bound(0, list1_num, val) - lower_bound(0, list1_num, val))
print(*d,sep=" ")
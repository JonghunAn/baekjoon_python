import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]
end = max(lan)

def lan_count(n):
    count = 0
    for item in lan:
        count += item // n
    return count

def binarySearch(start, end, N):
    if start > end:
        return end
    
    mid = (start + end) // 2
    lan_num = lan_count(mid)
    if lan_num >= N:
        return binarySearch(mid+1, end, N)
    else:
        return binarySearch(start, mid-1, N)

print(binarySearch(1, end, N))
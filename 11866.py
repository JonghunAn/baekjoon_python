import sys
import collections 
n,k = map(int,sys.stdin.readline().split())

person = collections.deque([i for i in range(1,n+1)])
del_person = []
idx= 0

while person:
    person.rotate(-(k-1))
    del_person.append(str(person.popleft()))

print("<"+", ".join(del_person)+">")
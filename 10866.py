import collections
import sys
from typing import Deque

input = sys.stdin.readline

arr = Deque();
for _ in range(int(input())):
    cmd = list(map(str, input().split()))
    if cmd[0] == "push_back":
        arr.append(int(cmd[1]))
    elif cmd[0] =='push_front':
        arr.appendleft(int(cmd[1]))
    elif cmd[0] == "pop_back":
        if(len(arr)==0):
            print(-1)
        else:
            print(arr.pop())
    elif cmd[0] =="pop_front":
        if(len(arr)==0):
            print(-1)
        else:
            print(arr.popleft())
            
    elif cmd[0] == "size":
        print(len(arr))
    elif cmd[0] == "empty":
        if len(arr)==0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if len(arr)==0:
            print(-1)
        else:
            print(arr[0])
    elif cmd[0] == "back":
        if len(arr) ==0:
            print(-1)
        else:
            print(arr[-1])

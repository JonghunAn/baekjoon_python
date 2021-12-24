import sys
input = sys.stdin.readline

arr = []
cnt = 0
for _ in range(int(input())):
    cmd = list(map(str, input().split()))
    if cmd[0] == "push":
        arr.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if arr:
            print(arr.pop(0))
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(arr))
    elif cmd[0] == "empty":
        if arr:
            print(0)
        else:
            print(1)
    elif cmd[0] == "front":
        if arr:
            print(arr[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if arr:
            print(arr[-1])
        else:
            print(-1)
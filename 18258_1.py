import sys
input = sys.stdin.readline

arr = []
cnt = 0
for _ in range(int(input())):
    cmd = list(map(str, input().split()))
    if cmd[0] == "push":
        arr.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if (len(arr)-cnt)==0:
            print(-1)
        else:
            print(arr[cnt])
            cnt+=1
    elif cmd[0] == "size":
        print(len(arr)-cnt)
    elif cmd[0] == "empty":
        if (len(arr)-cnt)==0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if (len(arr)-cnt)==0:
            print(-1)
        else:
            print(arr[cnt])
    elif cmd[0] == "back":
        if (len(arr)-cnt) ==0:
            print(-1)
        else:
            print(arr[-1])
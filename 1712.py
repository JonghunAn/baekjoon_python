a, b, c = map(int, input().split())
num = 0
d = 0

if(b>=c):
    print(-1)
else:
    d = int((a/(c-b)))+1
    print(d)
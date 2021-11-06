count = int(input())

point=[]
for i in range(count):
    #int가 아니면 틀린걸로 처리됨 -> 숫자를 순서로 인식
    

    #해결책 1       -> int값으로 받고 append
    x,y=map(int,input().split( ))
     #point.append(list(x))      list 함수 사용시 매개변수 한개
    point.append([x,y])
    #해결책 2       -> 그냥 받고 map으로 값 변환
    
    x,y=input().split( )
     #point.append(list(x))      list 함수 사용시 매개변수 한개
    point.append([x,y])
   

map(int,point)
point.sort(key=lambda x:(x[0],x[1]))
# 람다식을 숫자 형태로 바꿀 수는 없음 

for i in range(count):
    print(point[i][0],point[i][1],sep=" ")
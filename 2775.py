t = int(input())

for _ in range(t):
    floor = int(input())  # 층수
    num = int(input())  # 호수
    f0 = list(range(1, num+1))# 0층
    for k in range(floor):  # 층 수 만큼 반복
        for i in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
            f0[i] += f0[i-1]

    print(f0[-1])
#코드리뷰

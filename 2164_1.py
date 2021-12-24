from collections import deque

num = int(input())

temp = [i+1 for i in range(num)]
card = deque(temp)
while len(card)>1:
    card.popleft()
    card.append(card[0])
    card.popleft()    
    
    #pop(0) 시간복잡도 O(n)
    #deque의 leftpop 시간복잡도 O(1)
print(card[0])
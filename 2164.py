num = int(input())
card = [i+1 for i in range(num)]

while len(card)>1:
    card.pop(0)
    card.append(card[0])
    card.pop(0)    
    
    #pop(0) 시간복잡도 O(n)
    #deque의 leftpop 시간복잡도 O(1)
print(card[0])
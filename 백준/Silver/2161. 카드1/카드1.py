from collections import deque

N = int(input())
card = deque(range(1,N+1))

while len(card) > 1:
    print(card.popleft(), end=' ')
    card.rotate(-1)
print(*card)
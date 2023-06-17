from collections import deque

L = deque(range(1, int(input())+1))

while len(L) != 1:
    L.popleft()
    L.rotate(-1)

print(L[0])
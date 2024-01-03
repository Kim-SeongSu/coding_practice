from collections import deque

answer = []
N, K = map(int,input().split())
loop = deque(list(range(1,N+1)))

for _ in range(N):
    loop.rotate(-K+1)
    answer.append(str(loop.popleft()))

print('<'+', '.join(answer)+'>')
'''
# 메모리 초과
from collections import deque

N, K = map(int,input().split())
q = deque([(N,0)])

while q:
    x, cnt = q.popleft()
    if x == K:
        print(cnt)
        break
    else:
        cnt += 1
        for i in [-1,1,x]:
            q.append([x+i,cnt])


# 시간 초과
from collections import deque

N, K = map(int,input().split())
q = deque([(N,0)])

while q:
    x, cnt = q.popleft()
    if x == K:
        print(cnt)
        break
    else:
        cnt += 1
        for i in [-1,1,x]:
            if x+i >= 0 and x+i <= K and (x+i,cnt) not in q:
                q.append((x+i,cnt))
'''
from collections import deque

N, K = map(int,input().split())
if N >= K:
    print(N-K)
else:
    q = deque([(N,0)])
    visited = set([N])
    
    while q:
        x, cnt = q.popleft()
        if x == K:
            print(cnt)
            break
        else:
            cnt += 1
            for i in [-1,1,x]:
                if (x+i not in visited) and (N//2 < x+i < 1+K+K//2):
                    q.append((x+i,cnt))
                    visited.add(x+i)
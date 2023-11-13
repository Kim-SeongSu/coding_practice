'''
# 시간 초과
import sys

N, m, M, T, R = map(int,sys.stdin.readline().split())
X, answer = m, 0

if m+T > M and M-R < m:
    print(-1)
else:
    while N > 0:
        if X+T <= M:
            N -= 1
            X += T
        else:
            if X-R < m:
                X = m
            else:
                X -= R

        answer += 1
    print(answer)
'''
import sys

N, m, M, T, R = map(int,sys.stdin.readline().split())
X, answer, times = m, 0, 0

while N > 0:
    if m+T > M:
        break
    if X+T <= M:
        N -= 1
        X += T
    else:
        X = max(X-R,m)
    answer += 1
print(answer if N == 0 else -1)   
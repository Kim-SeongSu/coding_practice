N, M, K = map(int,input().split())

cnt = 0
while N+M > K+2:
    N -= 2
    M -= 1
    if N < 0 or M < 0:
        break
    cnt += 1
print(cnt)
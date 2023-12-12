N, K = map(int,input().split())
W, M = [0]*6, [0]*6
for _ in range(N):
    S, Y = map(int,input().split())
    if S == 0: W[Y-1] += 1
    else: M[Y-1] += 1

print(sum([i//K if i%K==0 else 1+i//K for i in W+M]))
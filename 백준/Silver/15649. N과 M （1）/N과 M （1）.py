from itertools import permutations as P

N, M = map(int,input().split())
num = [str(i) for i in range(1,N+1)]

for i in P(num,M):
    print(' '.join(i))
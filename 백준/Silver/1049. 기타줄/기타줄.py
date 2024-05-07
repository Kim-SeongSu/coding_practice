N, M = map(int,input().split())
min_pack, min_single = 1000, 1000

for _ in range(M):
  p, s = map(int,input().split())
  min_pack = min(min_pack,p)
  min_single = min(min_single,s)

S = 0
if N > 5:
  S += min(min_pack,min_single*6)*(N//6)
  N %= 6
if N != 0:
  S += min(min_pack,min_single*N)
print(S)
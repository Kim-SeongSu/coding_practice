import sys

N, M = map(int,input().split())
d = {}

for _ in range(N):
    ipt = sys.stdin.readline().rstrip()
    if len(ipt)>M-1:
        if ipt not in d:
            d[ipt] = 1
        else:
            d[ipt] += 1

print(*sorted(d, key= lambda x: (-d[x], -len(x), x )), sep='\n')
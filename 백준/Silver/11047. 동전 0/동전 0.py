import sys

N, K = map(int,sys.stdin.readline().split())
arr = sorted([int(sys.stdin.readline().rstrip()) for _ in range(N)],reverse=True)

c = 0

for i in arr:
    c += K//i
    K %= i

print(c)
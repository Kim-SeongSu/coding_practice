'''
# 시간 초과
import sys

N, M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

for _ in range(M):
    i, j = map(int,sys.stdin.readline().split())
    print(sum([i for i in arr[i-1:j]]))
'''

# Prefix Sum (누적 합)
import sys

N, M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

ps = [0]*(N+1)
ps[1] = arr[0]

for i in range(2,N+1):
    ps[i] = ps[i-1] + arr[i-1]

for _ in range(M):
    i, j = map(int,sys.stdin.readline().split())
    print(ps[j]-ps[i-1])
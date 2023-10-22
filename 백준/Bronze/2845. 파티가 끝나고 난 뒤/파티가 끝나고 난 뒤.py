import sys

L, P = map(int,sys.stdin.readline().split())
n = L*P

print(' '.join([str(i-n) for i in list(map(int,sys.stdin.readline().split()))]))
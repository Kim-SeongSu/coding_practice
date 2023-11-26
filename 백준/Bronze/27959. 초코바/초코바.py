import sys

N, M = map(int,sys.stdin.readline().split())
print('Yes' if N*100 >= M else 'No')
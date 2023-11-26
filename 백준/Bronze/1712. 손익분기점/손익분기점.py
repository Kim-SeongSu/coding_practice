import sys

A, B, C = map(int,sys.stdin.readline().split())
x = C-B

print(A//x+1 if x > 0 else -1)
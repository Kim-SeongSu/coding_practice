import sys

A, B, C = map(int,sys.stdin.readline().split())
print(A*B-C if A*B-C > 0 else 0)
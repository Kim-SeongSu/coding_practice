import sys

A, B = map(int,sys.stdin.readline().split())
C = int(sys.stdin.readline())
print(A+B if A+B < 2*C else (A+B)-2*C)
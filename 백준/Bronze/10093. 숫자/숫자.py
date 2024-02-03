import sys

A, B = sorted(map(int,sys.stdin.readline().split()))
print(B-A-1 if B>A else 0)

arr = []
while B-1>A:
    A += 1
    arr.append(A)
print(*arr)
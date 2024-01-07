import sys

n = int(sys.stdin.readline())
A,B = sorted(map(int,sys.stdin.readline().split())), sorted(map(int,sys.stdin.readline().split()),reverse=True)
print(sum([A[i]*B[i] for i in range(n)]))
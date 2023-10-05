import sys

N, M = map(int,sys.stdin.readline().split())

arr = {}
for _ in range(N):
    x = sys.stdin.readline().rstrip().split()
    arr[x[0]] = x[1]

for _ in range(M):
    print(arr[sys.stdin.readline().rstrip()])
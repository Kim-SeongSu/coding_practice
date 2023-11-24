import sys

N, K = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split(',')))

while K != 0:
    new = [0]*(N-1)
    for i in range(N-1):
        new[i] = arr[i+1]-arr[i]
    arr = new
    K -= 1
    N -= 1
print(','.join([str(x) for x in arr]))
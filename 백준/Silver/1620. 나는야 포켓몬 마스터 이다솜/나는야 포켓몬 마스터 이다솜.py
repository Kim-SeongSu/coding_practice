import sys

N, M = map(int,sys.stdin.readline().split())
arr, number = [sys.stdin.readline().rstrip() for i in range(N)], list(range(1,N+1))

D = dict(zip(arr, number))

for _ in range(M):
    x = sys.stdin.readline().rstrip()

    if x.isdigit():
        print(arr[int(x)-1])
    else:
        print(D.get(x))
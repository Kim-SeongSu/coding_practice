*arr, N = map(int,input().split())
print(4*N - sum(arr) if 4*N > sum(arr) else 0)
import sys

N, K = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

S = [0]*(N+1)
sum_, max_ = sum(arr[:K]), sum(arr[:K])
for i in range(K,N):
    sum_ += (arr[i]-arr[i-K])
    if sum_ > max_:
        max_ = sum_
print(max_)
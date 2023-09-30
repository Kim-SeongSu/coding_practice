import sys

k, n= map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(k)]
start, end = 1, max(arr)

while start <= end:
    mid = (start + end) // 2

    if sum([i//mid for i in arr]) >= n:
        start = mid +1
    else:
        end = mid -1
print(end)
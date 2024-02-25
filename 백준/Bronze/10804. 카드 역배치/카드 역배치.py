arr = list(range(1,21))

for _ in range(10):
    x, y = map(int,input().split())
    arr = arr[:x-1] + arr[x-1:y][::-1] + arr[y:]
print(*arr)
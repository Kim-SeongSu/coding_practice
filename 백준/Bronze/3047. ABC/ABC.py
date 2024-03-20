arr = dict(zip(['A', 'B', 'C'],sorted(map(int,input().split()))))

for i in input():
    print(arr[i], end=' ')
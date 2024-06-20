K = int(input())

x, y, arr = [], [], []
for _ in range(6):
    d, m = map(int, input().split())
    arr.append(m)
    if d == 1 or d == 2: x.append(m);
    else: y.append(m);
    
max_x, max_y = max(x), max(y)
min_x = arr[arr.index(max_x)+3] if arr.index(max_x)<3 else arr[arr.index(max_x)-3]
min_y = arr[arr.index(max_y)+3] if arr.index(max_y)<3 else arr[arr.index(max_y)-3]

print(K*(max_x*max_y - min_x*min_y))
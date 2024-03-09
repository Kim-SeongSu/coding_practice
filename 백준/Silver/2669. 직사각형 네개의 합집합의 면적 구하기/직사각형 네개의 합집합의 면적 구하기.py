arr = [[0]*100 for _ in range(1001)]

for _ in range(4):
    x1, y1, x2, y2 = map(int,input().split())

    for j in range(y1,y2):
        arr[j][x1:x2] = [1]*(x2-x1)
    
print(sum([arr[i].count(1) for i in range(1001)]))
arr = list(map(int,input().split()))

i, j = 0, 1
while arr != [1,2,3,4,5]:
    for i in range(4):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(*arr)
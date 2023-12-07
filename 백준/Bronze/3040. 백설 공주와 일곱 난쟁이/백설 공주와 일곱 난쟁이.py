arr = [int(input()) for _ in range(9)]
x, y = sum(arr), []

for i in range(8):
    for j in range(1,9):
        if i < j:
            if x - arr[i] - arr[j] == 100:
                y = [i, j]
                break

for k in range(9):
    if k not in y:
        print(arr[k])
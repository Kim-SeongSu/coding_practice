import sys

arr = sorted(map(int,sys.stdin.readline().split()))

for i in range(arr[0],arr[2]*arr[3]*arr[4]):
    x = 0
    for j in arr:
        if i % j == 0:
            x += 1
    if x > 2:
        print(i)
        break
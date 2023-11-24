arr = [0]*16
arr[0] = 2
for i in range(1,16):
    arr[i] = arr[i-1]+arr[i-1]-1

print(arr[int(input())]**2)
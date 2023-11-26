import sys

arr = sys.stdin.readline()
x = len(arr)//10
for i in range(0,x*10,10):
    print(arr[i:i+10])
print(arr[x*10:])
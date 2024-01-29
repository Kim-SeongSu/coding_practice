arr = [0]*100

s = 0
for _ in range(10):
    x = int(input())
    s +=  x
    arr[x//10] += 1
print(s//10, arr.index(max(arr))*10, sep='\n')
arr = []

for _ in range(5):
    n = int(input())

    if n not in arr:
        arr.append(n)
    else:
        arr.remove(n)
print(arr[0])
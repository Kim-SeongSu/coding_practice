import sys

for _ in range(int(sys.stdin.readline())):
    arr, result = {}, 1
    
    for _ in range(int(sys.stdin.readline())):
        x = sys.stdin.readline().split()[-1]

        if x not in arr.keys():
            arr[x] = 1
        else:
            arr[x] += 1

    for i in list(arr.values()):
        result *= i+1
    print(result-1)
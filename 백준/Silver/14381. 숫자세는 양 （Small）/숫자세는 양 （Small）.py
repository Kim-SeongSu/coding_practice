import sys

for i in range(1,int(input())+1):
    N = int(sys.stdin.readline())
    arr, x = {'1','2','3','4','5','6','7','8','9','0'}, 1
    while x < 10000:
        arr = arr.difference(set(list(str(N*x))))
        if len(arr) == 0:
            break 
        x += 1
    
    print(f'Case #{i}: {N*x}' if len(arr) == 0 else f'Case #{i}: INSOMNIA')
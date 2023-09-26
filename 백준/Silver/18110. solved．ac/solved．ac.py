import sys

def rounds(n):
    return int(n)+1 if n - int(n) >= 0.5 else int(n)

n = int(sys.stdin.readline())
if n == 0:
    print(0)
else:
    arr = sorted([int(sys.stdin.readline()) for _ in range(n)])
    if n > 3:
        arr = arr[rounds(n*0.15):-rounds(n*0.15)]
    print(rounds(sum(arr)/len(arr)) if len(arr) != 0 else 0)
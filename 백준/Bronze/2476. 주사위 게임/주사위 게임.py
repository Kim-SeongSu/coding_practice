import sys

input = sys.stdin.readline

n = int(input())
arr = [0]*n

for i in range(n):
    x = sorted(map(int,input().split()))
    if x[0] == x[1] == x[2]:
        arr[i] = 10000+x[0]*1000
    elif len(set(x)) == 2:
        k = [num for num in range(1,7) if x.count(num) == 2][0]
        arr[i] = 1000+k*100
    else:
        arr[i] = max(x)*100
print(max(arr))
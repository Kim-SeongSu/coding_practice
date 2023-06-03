import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k,n = int(input()),int(input())
    arr = list(range(1,1+n))

    for _ in range(k):
        for i in range(1,n):
            arr[i] += arr[i-1]
    print(arr[-1])
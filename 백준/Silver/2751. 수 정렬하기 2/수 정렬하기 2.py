import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * N

for i in range(N):
    arr[i] = int(input())

for i in sorted(arr):
    print(i)
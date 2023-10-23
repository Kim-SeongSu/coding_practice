import sys

N = int(sys.stdin.readline())
arr = sorted(map(int,sys.stdin.readline().split()))

print(arr[N//2-1]*arr[N//2] if N % 2 == 0 else arr[N//2]**2)
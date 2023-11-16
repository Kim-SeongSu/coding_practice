import sys

input = sys.stdin.readline

arr = [0]
for i in range(1,50):
    arr += [i]*i

A, B = map(int,input().split())

print(sum(arr[A:B+1]))
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))

answer = arr[0]
x = arr[0]
for i in range(1,n):
    if arr[i] == 0:
        x = 0
    else:
        if arr[i-1] == 1:
            x += 1
        else:
            x = 1
    answer += x
print(answer)
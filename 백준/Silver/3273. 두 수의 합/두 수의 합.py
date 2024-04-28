'''
# 시간초과
from itertools import combinations as cb

n = int(input())
arr = map(int,input().split())
x = int(input())

print(sum([1 for i in cb(arr,2) if sum(i) == x]))


# 시간초과
n = int(input())
arr = sorted(map(int,input().split()))
x = int(input())

print(sum([1 for i in arr if x-i in arr])//2)
'''

n = int(input())
arr = map(int,input().split())
x = int(input())

cnt = 0
l = [0]*(1+x)
for i in arr:
    if x>i:
        if l[i] == 0:
            l[i], l[x-i] = 1, 1
        elif l[i] == 1:
            cnt += 1 
print(cnt)
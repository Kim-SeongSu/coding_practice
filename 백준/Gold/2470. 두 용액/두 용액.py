'''
# 시간 초과
from itertools import combinations as cb

N = int(input())
l = sorted(map(int,input().split()))

min_, result = 9999999999, (0, 0)
for i in cb(l,2):
    x = abs(sum(i))
    if min(min_,x) == x:
        min_ = x
        result = i
print(*result)
'''

n = int(input())
l = sorted(map(int,input().split()))

s, e = 0, n-1
a, b, min_ = 0, 0, 10**10

while s<e:
    sum_ = l[s]+l[e]
    
    if  min(min_,abs(sum_)) == abs(sum_):
        a, b = l[s], l[e]
        min_ = abs(sum_)

    if sum_ == 0:
        break
    elif sum_ > 0:
        e -= 1
    else: 
        s += 1
print(a, b)
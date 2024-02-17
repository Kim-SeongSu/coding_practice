'''
# 메모리초과
import sys

N, M = map(int,sys.stdin.readline().split())

A = sorted(map(int,sys.stdin.readline().split()))
B = sorted(map(int,sys.stdin.readline().split()))

arr = [0]*100000000

s = 0
if min(N,M) == N:
    for i in A:
        if i in B:
            s += 1
else:
    for i in B:
        if i in A:
            s += 1

print(len(set(A+B))-s)
'''

import sys

N, M = map(int,sys.stdin.readline().split())

A = sorted(map(int,sys.stdin.readline().split()))
B = sorted(map(int,sys.stdin.readline().split()))

x=A+B
y=set(x)

print(len(x)-2*(len(x)-len(y)))
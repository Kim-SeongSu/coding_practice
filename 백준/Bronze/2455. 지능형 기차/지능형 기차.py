import sys

x,y = 0,0
for _ in range(4):
    A,B = map(int,sys.stdin.readline().split())
    x = x-A+B
    y = max(y,x)
print(y)
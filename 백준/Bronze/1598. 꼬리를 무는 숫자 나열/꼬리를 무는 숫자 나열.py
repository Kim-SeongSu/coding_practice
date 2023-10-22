import sys

a, b = sorted(map(int,sys.stdin.readline().split()))
x, y = 0, 0

for i in range(4):
    if (a+i)%4 == 0:
        x = a+i
    if (b+i)%4 == 0:
        y = b+i
print((y-x)//4 + abs((x-a)-(y-b)))
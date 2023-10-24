import sys

x, y = map(int,sys.stdin.readline().split())
a = (x+y)//2
b = x-a
print(' '.join([str(a), str(b)]) if (x+y)%2 == 0 and b > -1 else -1)
import sys

n = 1

for i in range(int(sys.stdin.readline().rstrip())):
    x, y = map(int,sys.stdin.readline().split())
    if n not in [x,y]:
        pass
    else:
        if n == x:
            n = y
        else:
            n = x
print(n if n in [1,2,3] else -1)
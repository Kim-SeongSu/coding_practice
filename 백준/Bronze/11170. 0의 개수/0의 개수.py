import sys

for _ in range(int(sys.stdin.readline())):
    a, b = map(int,sys.stdin.readline().split())
    print(''.join([str(i) for i in range(a,b+1)]).count('0'))
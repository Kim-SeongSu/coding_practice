import sys

a,b = map(str,sys.stdin.readline().split())
print(bin(int(a,2)+int(b,2))[2:])
import sys

A,B,C = map(int,sys.stdin.readline().split())
D = int(sys.stdin.readline())
S = A*3600 + B*60 + C + D

print(S//3600%24, S%3600//60, S%3600%60, sep=' ')
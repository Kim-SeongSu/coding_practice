import sys

N = int(sys.stdin.readline())

for i in range(N):
    star = ' '*i+'*'*(N-1-i)
    print(star+'*'+star[::-1].rstrip())
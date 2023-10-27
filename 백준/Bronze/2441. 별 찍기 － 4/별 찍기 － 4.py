import sys

N = int(sys.stdin.readline())
star = '*'*N

for i in range(N):
    print(' '*i+star[i:])
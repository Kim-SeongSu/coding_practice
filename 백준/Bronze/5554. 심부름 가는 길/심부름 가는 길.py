import sys

S = sum([int(sys.stdin.readline()) for _ in range(4)])
print(S//60, S%60, sep='\n')
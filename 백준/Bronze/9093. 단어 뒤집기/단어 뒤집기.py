import sys

for _ in range(int(sys.stdin.readline())):
    print(' '.join([string[::-1] for string in map(str,sys.stdin.readline().rstrip().split())]))
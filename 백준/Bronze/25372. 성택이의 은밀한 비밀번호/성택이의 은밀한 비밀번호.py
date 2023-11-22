import sys

for _ in range(int(sys.stdin.readline())):
    x = sys.stdin.readline().strip()
    print('yes' if 5 < len(x) < 10 else 'no')
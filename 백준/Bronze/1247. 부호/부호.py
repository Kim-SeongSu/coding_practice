import sys

for _ in range(3):
    x = sum([int(sys.stdin.readline()) for i in range(int(sys.stdin.readline()))])
    print('0' if x == 0 else '+' if x > 0 else '-')
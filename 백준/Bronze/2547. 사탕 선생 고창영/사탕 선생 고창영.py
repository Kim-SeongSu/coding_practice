import sys

input = sys.stdin.readline

for _ in range(int(input())):
    blank, n = input(), int(input())
    s = sum([int(input()) for _ in range(n)])
    print('YES' if s%n == 0 else 'NO')
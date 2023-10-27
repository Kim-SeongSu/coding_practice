import sys

N, M = map(int,sys.stdin.readline().split())
row, col = 0, int(bin(1<<M),2)

for _ in range(N):
    string = sys.stdin.readline().rstrip()
    if string == '.'*M:
        row += 1
    col |= int('1'+string.replace('X','1').replace('.','0'), 2)

print(max(bin(col)[3:].count('0'),row))
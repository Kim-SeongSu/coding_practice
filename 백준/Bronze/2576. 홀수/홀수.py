import sys

input = sys.stdin.readline
odd = []
for _ in range(7):
    x = int(input())
    if x % 2 == 1:
        odd.append(x)

print(f'{sum(odd)}\n{min(odd)}' if odd != [] else -1)
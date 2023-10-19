import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s == '#':
        break
    print(sum([1 for i in s.lower() if i in ['a','e','i', 'o', 'u']]))
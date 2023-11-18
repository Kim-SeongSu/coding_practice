import sys

while True:
    x = sys.stdin.readline().rstrip()
    
    if x == 'END':
        break
    print(x[::-1])
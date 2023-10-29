import sys

while True:
    string = sys.stdin.readline().rstrip()

    if string == '0 0':
        break
    print(sum(map(int,string.split())))
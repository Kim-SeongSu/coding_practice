import sys

for s in sys.stdin.read().splitlines():
    A,a,n,b = 0, 0, 0, 0
    for i in s:
        if i == ' ':
            b += 1
        elif i.isdigit() == 1:
            n += 1
        elif i.isupper() == 1:
            A += 1
        else:
            a += 1
    print(a, A, n, b)
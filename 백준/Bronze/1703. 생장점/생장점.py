import sys

while True:
    I = sys.stdin.readline().rstrip()
    if I =='0':
        break
    else:
        a, *arr = map(int,I.split())
    
    n = 1
    for i in range(2*a):
        if i % 2 == 0:
            n *= arr[i]
        else:
            n -= arr[i]
    print(n)
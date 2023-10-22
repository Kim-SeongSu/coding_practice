import sys

while True:
    n = sys.stdin.readline().rstrip()
    
    if n == '0':
        break
    one = n.count('1')
    zero = n.count('0')
    print(2 +  2*one + 4*zero + 3*(len(n)-one-zero) + len(n)-1)
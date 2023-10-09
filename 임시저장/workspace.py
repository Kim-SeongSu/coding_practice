import sys

N = int(sys.stdin.readline())

connect, not_connect, temp = set(), set(), set()

for _ in range(int(sys.stdin.readline())):
    a,b = sorted(map(int,sys.stdin.readline().split()))
    
    if a == 1:
        connect.add(b)
    elif a in connect or b in connect:
        connect |= set([a,b])
    elif a in not_connect or b in not_connect:
        not_connect |= set([a,b])
    else:
        temp |= set([a,b])


    if len(temp & not_connect) > 0:
        not_connect |= temp
    elif len(temp & connect) > 0:
        connect |= temp

print(len(connect))
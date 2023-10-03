'''
# 메모리초과
import sys

S = set()

for _ in range(int(sys.stdin.readline())):
    temp = sys.stdin.readline().split()
    
    if len(temp) == 1:
        if temp[0] == 'all':
            S = set(range(1,21))
        else:
            S = set()
    else:
        order, x = temp[0], int(temp[1])

        if order == 'check':
            print(1 if x in S else 0)
        elif order == 'add':
            S.add(x)
        elif order == 'remove':
            S.discard(x)
        else:
            if x in S:
                S.discard(x)
            else:
                S.add(x)
'''
# 비스마스킹 사용
import sys

S = 0

for _ in range(int(sys.stdin.readline())):
    temp = sys.stdin.readline().split()
    
    if len(temp) == 1:
        if temp[0] == 'all':
            S = (1 << 21) -1
        else:
            S = 0
    else:
        order, x = temp[0], int(temp[1])

        if order == 'check':
            print(0 if S & (1 << x) == 0 else 1)
        elif order == 'add':
            S |= (1 << x)
        elif order == 'remove':
            S &= ~(1 << x)
        else:
            S = S ^ (1 << x)
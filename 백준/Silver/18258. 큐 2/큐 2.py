# 시간초과
'''
queue = []

for _ in range(int(input())):
    x = input().split()
    if len(x) == 2:
        queue.append(x[1])
    else:
        if x[0] == 'pop':
            if len(queue)==0:
                print(-1)
            else:
                print(queue[0])
                del queue[0]
        elif x[0] == 'size':
            print(len(queue))
        elif x[0] == 'empty':
            print(1 if len(queue)==0 else 0)
        elif x[0] == 'front':
            print(queue[0] if len(queue)!=0 else -1)
        else:
            print(queue[-1] if len(queue)!=0 else -1)
'''
import sys
from collections import deque

queue = deque([])

for _ in range(int(sys.stdin.readline())):
    x = sys.stdin.readline().split()
    if x[0] == 'push':
        queue.append(x[1])
    else:
        if x[0] == 'pop':
            if len(queue)==0:
                print(-1)
            else:
                print(queue.popleft())
        elif x[0] == 'size':
            print(len(queue))
        elif x[0] == 'empty':
            print(1 if len(queue)==0 else 0)
        elif x[0] == 'front':
            print(queue[0] if len(queue)!=0 else -1)
        else:
            print(queue[-1] if len(queue)!=0 else -1)
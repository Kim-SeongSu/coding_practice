from collections import deque
import sys
arr = deque()

for _ in range(int(sys.stdin.readline())):
    order = sys.stdin.readline().split()

    if order[0] == 'push_front':
        arr.appendleft(order[1])
    elif order[0] == 'push_back':
        arr.append(order[1])
    elif order[0] == 'pop_front':
        print(-1 if len(arr)==0  else arr.popleft())
    elif order[0] == 'pop_back':
        print(-1 if len(arr)==0  else arr.pop())
    elif order[0] == 'size':
        print(len(arr))
    elif order[0] == 'empty':
        print(1 if len(arr)==0 else 0)   
    elif order[0] == 'front':
        print(-1 if len(arr)==0  else arr[0])
    else:
        print(-1 if len(arr)==0  else arr[-1])
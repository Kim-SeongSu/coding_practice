from collections import deque

arr = deque(['N','E','S','W'])

for _ in range(int(10)):
    order = input()

    if order == '1':
        arr.rotate(-1)
    elif order == '2':
        arr.rotate(2)
    else:
        arr.rotate(1)    
print(arr[0])
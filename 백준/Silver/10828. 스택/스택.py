import sys
stack = []

for _ in range(int(sys.stdin.readline())):
    order = sys.stdin.readline().split()

    if 'push' == order[0]:
        stack.append(int(order[-1]))

    elif 'pop' == order[0]:
        print(-1 if stack == [] else stack.pop())

    elif 'top' == order[0]:
        print(-1 if stack == [] else stack[-1])

    elif 'size' == order[0]:
        print(len(stack))

    elif 'empty' == order[0]:
        print(1 if stack == [] else 0)

    else:
        print('error')
        break
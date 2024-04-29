import sys
input = sys.stdin.readline 


stack = []

for i in range(int(input())):
    ipt = input().rstrip()
    if ipt[0] == '1':
        stack.append(int(ipt[2:]))
    elif ipt == '2':
        print(-1 if stack == [] else stack.pop())
    elif ipt == '3':
        print(len(stack))
    elif ipt == '4':
        print(1 if stack == [] else 0)
    else:
        print(-1 if stack == [] else stack[-1])
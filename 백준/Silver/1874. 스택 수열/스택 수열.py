stack, records, n = [], [], 1

for _ in range(int(input())):
    x = int(input())

    while n <= x: 
        stack.append(n)
        records.append('+')
        n += 1

    if stack[-1] == x:
        stack.pop()
        records.append('-')
    else:
        records = [0]
        break

print('NO' if [0] == records else '\n'.join(records))
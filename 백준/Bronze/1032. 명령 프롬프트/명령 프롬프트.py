import sys

n = int(sys.stdin.readline())
result = list(sys.stdin.readline().strip())

for _ in range(n-1):
    inputs = list(sys.stdin.readline().strip())
    for i in range(len(result)):
        if result[i] != inputs[i]:
            result[i] = '?'
print(''.join(result))
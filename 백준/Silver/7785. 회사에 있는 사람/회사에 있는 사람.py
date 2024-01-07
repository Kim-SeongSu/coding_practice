import sys

arr = []
for _ in range(int(sys.stdin.readline())):
    name, log = sys.stdin.readline().split()
    if log == 'enter':
        arr.append(name)
    else:
        arr.remove(name)
for i in sorted(arr,reverse=True):
    print(i)
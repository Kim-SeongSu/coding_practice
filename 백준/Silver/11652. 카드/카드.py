import sys

D = {}
for _ in range(int(input())):
    ipt = sys.stdin.readline().strip()
    if ipt in D:
        D[ipt] += 1
    else:
        D[ipt] = 1

print(sorted(D, key = lambda x: (-D[x],int(x)))[0])
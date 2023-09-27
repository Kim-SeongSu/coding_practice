import sys

n, arr = sys.stdin.readline(), list(map(int,sys.stdin.readline().split()))
d = dict(zip(set(arr),[0]*len(set(arr))))
for i in arr:
    d[i] += 1

m, arr2 = sys.stdin.readline(), list(map(int,sys.stdin.readline().split()))
print(' '.join([str(d.get(i)) if i in d else '0' for i in arr2]))
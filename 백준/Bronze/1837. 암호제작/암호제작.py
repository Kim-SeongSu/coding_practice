import sys

P, K = map(int,sys.stdin.readline().split())

for i in range(2, K):
    if P % i == 0:
        print("BAD", i)
        break
else:
    print("GOOD")
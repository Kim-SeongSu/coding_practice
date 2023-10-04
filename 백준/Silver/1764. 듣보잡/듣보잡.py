import sys

N, M = map(int,sys.stdin.readline().split())
h,s = [sys.stdin.readline().rstrip() for _ in range(N)], [sys.stdin.readline().rstrip() for _ in range(M)]

answer = sorted(set(h) & set(s))
print(len(answer))
for i in answer:
    print(i)
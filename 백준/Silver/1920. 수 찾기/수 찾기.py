import sys
input = sys.stdin.readline


N, A = input(), set(map(int,input().split()))
M,arr = input(), list(map(int,input().split()))

for i in arr:
    print(int(i in A))
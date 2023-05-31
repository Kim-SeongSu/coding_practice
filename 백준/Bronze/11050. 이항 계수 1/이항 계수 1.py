import sys
input = sys.stdin.readline

N, K = map(int,input().split())

Denominator, Numerator = 1, 1
for i in range(N-K+1,N+1):
    Denominator *= i
for i in range(1,K+1):
    Numerator *= i

print(int(Denominator / Numerator))
N = int(input())
T = sum(map(int,input().split()))
S = 8*(N-1)+T

print(S//24, S%24)
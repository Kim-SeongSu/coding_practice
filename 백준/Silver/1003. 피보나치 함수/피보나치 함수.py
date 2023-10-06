# 메모리 초과
'''
import sys

for _ in range(int(sys.stdin.readline())): 
    N = int(sys.stdin.readline())
    dp = [0]*(N+3)
    dp[0], dp[1] = '0', '1'
    
    for i in range(2,N+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[N].count('0'), dp[N].count('1'))
'''

import sys

def fibo(N):
    for i in range(3,N+1):
        zero[i] = zero[i-1] + zero[i-2]
        one[i] = one[i-1] + one[i-2]
    return print(zero[N], one[N])

for _ in range(int(sys.stdin.readline())): 
    N = int(sys.stdin.readline())
    
    if N > 2:
        zero = [1,0,1]+[0]*(N-2)
        one = [0,1,1]+[0]*(N-2)
    else:
        zero = [1,0,1]
        one = [0,1,1]
    fibo(N)
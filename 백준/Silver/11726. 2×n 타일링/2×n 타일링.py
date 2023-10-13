'''
# 2x1
1
# 2x2
2
# 2x3
3
# 2x4
5
# 2x5
8 

f(1) = 1
f(2) = 2 일 때,
f(n) = f(n-1) + f(n-2)
'''
import sys

n = int(sys.stdin.readline())
if n < 3:
    print(n)
else:
    dp = [0]*(n+1)

    dp[1], dp[2] = 1, 2

    for i in range(3,n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007

    print(dp[n])
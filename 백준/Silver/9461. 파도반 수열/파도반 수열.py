import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0] * 101

    dp[1] = 1
    dp[2] = 1
    dp[3] = 1

    for index in range(4,101):
        dp[index] = dp[index-3] + dp[index -2]
    
    print(dp[N])
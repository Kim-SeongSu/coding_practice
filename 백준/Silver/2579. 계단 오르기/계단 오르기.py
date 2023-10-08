# 다이나믹 프로그래밍
import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
dp = [0] * N     

if len(arr) < 3:
    print(sum(arr))
else:
    dp[0], dp[1] = arr[0], sum(arr[:2])
    for i in range(2,N):
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])
    print(dp[-1])
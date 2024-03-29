'''
# 9095번 - 다이나믹 프로그래밍
# 1 (1개)
1

# 2 (2개)
1+1
2

# 3 (4개)
1+1+1
1+2
2+1
3

# 4 (7개)
1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1

# 5 (13개)
1+1+1+1+1
1+1+1+2
1+1+2+1
1+2+1+1
2+1+1+1
2+2+1
2+1+2
1+2+2
1+1+3
1+3+1
3+1+1
2+3
3+2

f(1) = 1
f(2) = 2
f(3) = 4 일 때,
f(n) = f(n-1) + f(n-2)+ f(n-3)
'''
import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    dp = [0,1,2,4] + [0]*(n-3)

    for i in range(4,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    print(dp[n])
'''
1 5               5
2 5 4+3          12
3 5 4+3 4+6      22
4 5 4+3+ 4+6 4+9 35
'''
N = int(input())

dp = [0]*(N+1) 
dp[1], x = 5, 1

for i in range(2,N+1):  
    dp[i] = dp[i-1]+ 4+3*x
    x += 1
print(dp[N]%45678)
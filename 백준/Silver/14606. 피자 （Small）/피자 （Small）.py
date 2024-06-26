'''
1  0*1                                   0
2  1*1                                   1   1
3  2*1 + 1*1                             3   2
4  2*2 + 1*1 + 1*1                       6   3
5  2*3 + 1*1 + 2*1 + 1*1                10   4
6  3*3 + 2*1 + 1*1 + 2*1 + 1*1          15   5
7  3*4 + 2*1 + 1*1 + 2*2 + 1*1 + 1*1    21   6
8  4*4
9  4*5
10 5*5

'''

N = int(input())
dp = [0]*(N+1)
x = 1

for i in range(1,N+1):
    dp[i] = dp[i-1] + x
    x += 1
print(dp[N-1])
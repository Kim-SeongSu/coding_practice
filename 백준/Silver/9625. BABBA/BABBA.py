'''
N    0 1 2  3   4     5        6             7
     A B BA BAB BABBA BABBABAB BABBABABBABBA BABBABABBABBABABBABAB
A    1 0 1  1   2     3        5             8
B    0 1 1  2   3     5        8             13

'''


K = int(input())

if K == 0:
    print('1 0')
elif K == 1:
    print('0 1')
else:
    dp = [0]*(K+1)
    dp[0], dp[1] = 0, 1

    for i in range(2,K+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(f'{dp[K-1]} {dp[K]}')
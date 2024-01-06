'''
# 방법 1 - 시간초과
import sys

n, cnt = int(sys.stdin.readline()), []

arr = [i**2 for i in range(int(n**0.5)+1)]

if N < 9:
    print((n//4)+(n%4))
else:
    for a in arr:
        for b in arr:
            for c in arr:
                for d in arr:
                    if a+b+c+d == n:
                        cnt.append(4-[a,b,c,d].count(0))
    print(min(cnt))
'''
# 다이나믹 프로그래밍
import sys

n = int(sys.stdin.readline())
dp = [0,1]

for i in range(2,n+1):
    min_ = 50000
    for j in range(1,int(i**0.5)+1):
        min_ = min(min_,dp[i-j**2])
    dp.append(min_+1)
print(dp[n]) 
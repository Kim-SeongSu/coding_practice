'''
# 시간 초과
N = int(input())
s = [0]*N
A = list(map(int,input().split()))

for i in range(N-2):
  cnt, x = 1, A[i]
  for j in A[i+1:]:
    if x < j:
      cnt += 1
      x = j
  s[i] = cnt
print(max(s))
'''

N = int(input())
arr = list(map(int, input().split()))
dp = [1]*N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
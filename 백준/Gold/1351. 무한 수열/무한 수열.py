'''
# 시간초과
N, P, Q = map(int,input().split())
A = [1]+[0]*N

for i in range(1,N+1):
    A[i] = A[i//P] + A[i//Q]

print(A[N])
'''

N, P, Q = map(int,input().split())
A = {0:1}

def dp(i):
    if i not in A:
        A[i] = 0
    if A[i] == 0:
        A[i] = dp(i//P) + dp(i//Q)
    return A[i]
    
dp(N)
print(A[N])
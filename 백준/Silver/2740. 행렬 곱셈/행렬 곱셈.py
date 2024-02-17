'''
# 런타임 에러 (ModuleNotFoundError)
import sys
import numpy as np

N, M = map(int,sys.stdin.readline().split())
A = np.array([list(map(int,sys.stdin.readline().split())) for _ in range(N)])

M, K = map(int,sys.stdin.readline().split())
B = np.array([list(map(int,sys.stdin.readline().split())) for _ in range(M)])

result = np.dot(A, B)

for i in result:
    print(*i)
'''
import sys

N, M = map(int,sys.stdin.readline().split())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

M, K = map(int,sys.stdin.readline().split())
B_inverse = [[0]*M for _ in range(K)]

for i in range(M):
    arr = list(map(int,sys.stdin.readline().split()))
    for j in range(K-1,-1,-1):
        B_inverse[j][i] = arr.pop() 

answer = [[0]*K for _ in range(N)]

for i in range(N):
    for j in range(K):
        answer[i][j] = sum([A[i][k]*B_inverse[j][k] for k in range(M)])
    print(*answer[i])
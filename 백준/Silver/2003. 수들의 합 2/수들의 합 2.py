import sys

N, M = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))

s, j, result = 0, 0, 0
for i in range(N):
    if A[i] >= M:
        j = i + 1
        s = 0
        if A[i] == M:
            result += 1
    else:
        s += A[i]
        if s == M:
            result += 1
        else:
            while s > M:
                s -= A[j]
                j += 1
                if s == M:
                    result += 1
                    break
            
print(result)
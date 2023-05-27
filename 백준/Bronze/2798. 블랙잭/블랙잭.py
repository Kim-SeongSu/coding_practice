N,M = map(int,input().split())
A = list(map(int,input().split()))

result = []

for i in range(N):
    for j in range(1,N):
        for k in range(2,N):
            if ((i != j) and (j != k) and (i != k)) & (A[i]+A[j]+A[k] <= M):
                result.append(A[i]+A[j]+A[k])

print(max(set(result)))
N = int(input())
A, B = list(map(int,input().split())), [-1]*N
P = sorted(A)

for i in range(N):
    for j in range(N):
        if P[i] == A[j] and B[j] == -1:
            B[j] = i
            break
print(*B)
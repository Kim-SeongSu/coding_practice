A, B, C, N = map(int,input().split())

TF = 0
for i in range(N//C+1):
    for j in range(N//B+1):
        for k in range(N//A+1):
            if C*i+B*j+A*k == N:
                TF = 1
                break
print(int(TF))
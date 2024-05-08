A, B, C, N = map(int,input().split())
x = N//A

TF = 0
for i in range(x):
    for j in range(x):
        for k in range(x):
            if C*i+B*j+A*k == N:
                TF = 1
                break
print(int(TF))
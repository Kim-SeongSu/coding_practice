A, B, N = map(int,input().split())

for i in range(N):
    A = (A%B)*10
    x = A//B
print(x)
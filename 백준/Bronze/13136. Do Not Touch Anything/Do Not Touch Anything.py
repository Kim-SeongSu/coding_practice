R, C, N = map(int,input().split())
X = R//N if R%N==0 else R//N+1
Y = C//N if C%N==0 else C//N+1
print(X*Y)
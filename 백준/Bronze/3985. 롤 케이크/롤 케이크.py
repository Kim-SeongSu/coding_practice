import sys
ipt = sys.stdin.readline

L, N = int(ipt()), int(ipt())

cake, pre, real = [1]*L, {}, {}

for i in range(1,N+1):
    P, K = map(int,ipt().split())
    real[str(i)] = K-P+1
    pre[str(i)] = cake[P:K+1].count(1)
    cake[P:K+1] = [0]*(K-P+1)
    
print(max(real.keys(), key=lambda x : real[x]), max(pre.keys(), key=lambda x : pre[x]), sep='\n')
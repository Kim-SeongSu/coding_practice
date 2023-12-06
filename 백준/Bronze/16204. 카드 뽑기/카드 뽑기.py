N, M, K = map(int,input().split())
print(min(K,M)+min(N-M,N-K))
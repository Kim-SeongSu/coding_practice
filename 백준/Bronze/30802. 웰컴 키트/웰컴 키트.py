N = int(input())
size = list(map(int,input().split()))
T, P = map(int,input().split())

sum_ = sum([i//T if i%T==0 else i//T+1 for i in size])
print(sum_)
print(N//P, N%P)
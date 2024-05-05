A, B = sorted(map(int,input().split()))
print((A+B)*(B-A+1)//2 if A!=B else A)
D = sorted(map(int,input().split(':')))
if D[0] > 59 or D[1] > 59 or D[2] > 59:
    print(0)
else:
    print(2*sum([1 for i in D if i>0 and i <13]))
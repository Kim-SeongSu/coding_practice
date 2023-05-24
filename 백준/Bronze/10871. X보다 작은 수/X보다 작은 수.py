X = list(map(int,input().split()))[1]
print(' '.join([i for i in input().split() if int(i) < X]))
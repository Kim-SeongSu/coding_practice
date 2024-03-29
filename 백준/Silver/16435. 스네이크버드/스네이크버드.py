N, L = map(int,input().split())

for i in sorted(map(int,input().split())):
    if L >= i:
        L+=1
print(L)
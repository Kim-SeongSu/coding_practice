C, S = 100, 100

for _ in range(int(input())):
    c, s = map(int,input().split())
    if c == s:
        pass
    elif c > s:
        S -= c
    else:
        C -= s
print(C,S,sep='\n')
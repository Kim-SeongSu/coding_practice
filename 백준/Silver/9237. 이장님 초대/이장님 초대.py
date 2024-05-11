N, D = int(input()), 1
t = sorted(map(int,input().split()),reverse=True)

max_ = t[0]
for i in t[1:]:
    max_ = max(max_-1,i)
    
print(D+N+max_)
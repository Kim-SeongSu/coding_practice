N = int(input())
P = [[0]*1001 for _ in range(1001)]

for i in range(1,N+1):
    x, y, a, b = map(int,input().split())
    for j in range(y,y+b):
        P[j][x:x+a] = [i]*a

for i in range(1,N+1):    
    print(sum([j.count(i) for j in P]))
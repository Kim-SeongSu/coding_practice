x, N = map(int,input().split())
t = 0

while t < N:    
    x = (x//2)^6 if x%2 == 0 else (2*x)^6
    t += 1
print(x)
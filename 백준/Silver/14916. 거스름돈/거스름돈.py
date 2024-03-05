n = int(input())
s, x = 9999999, 0
if n % 5 == 0:
    print(n//5)
else:
    for i in range(n,0,-5):
        if i%2 == 0:
            s = min(s,x+i//2)
        x += 1
    print(s if s != 9999999 else -1)
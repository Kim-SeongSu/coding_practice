from math import gcd

a, b = map(int,input().split())
c, d = map(int,input().split())

x = a*d + b*c
y = b*d
gcd_ = gcd(x,y)
print(x//gcd_,y//gcd_)
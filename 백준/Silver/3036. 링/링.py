from math import gcd

N = input()
x, *R = map(int,input().split())

for i in R:
    g = gcd(x,i)
    print(x//g,'/',i//g, sep='')
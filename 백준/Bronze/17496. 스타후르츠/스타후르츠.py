n, t, c, p = map(int,input().split())
s, n = 0, n-1
while n >= t:
    s += c*p
    n -= t
print(s)
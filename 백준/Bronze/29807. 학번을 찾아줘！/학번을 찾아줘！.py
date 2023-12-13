n = int(input())
score = list(map(int,input().split())) + [0]*(5-n)
k,m,e,s,l = map(int,score)

x =  l*707
x += 508*(k-e) if k > e else 108*(e-k)
x += 212*(m-s) if m > s else 305*(s-m)

print(x*4763)
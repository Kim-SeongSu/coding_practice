N = int(input())

a,b = 1,1
if N%2==0:
    a += N//2
    b = a
else:
    a += N//2
    b = a+1
print(a*b)
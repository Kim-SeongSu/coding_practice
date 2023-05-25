'''
a,b,c,d,e= map(int,input().split())
print((a**2+b**2+c**2+d**2+e**2)%10)
'''

def square(n):
    S = n**2
    return S

def sol(n):
    a,b,c,d,e= map(int,n.split())
    A,B,C,D,E = square(a),square(b),square(c),square(d),square(e)
    result = (A+B+C+D+E)%10
    return result


print(sol(input()))
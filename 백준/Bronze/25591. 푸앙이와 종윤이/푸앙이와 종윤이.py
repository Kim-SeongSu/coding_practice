x, y = map(int,input().split())

a, b = 100 - x, 100 - y
c, d = 100 - (a+b), a*b 
q, r = d // 100, d % 100
result = str(x*y) if len(str(x*y)) > 3 else '0'+ str(x*y)

print(a, b, c, d, q, r)
print(int(result[:2]), int(result[-2:]))
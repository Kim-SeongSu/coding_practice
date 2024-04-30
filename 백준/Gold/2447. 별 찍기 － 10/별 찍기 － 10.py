n = int(input())
s = [['*']*n for _ in range(n)]

def func(x,y,n):
  n //= 3
  for i in range(x+n, x+2*n):
    for j in range(y+n, y+2*n):
      s[i][j] = ' '
  if n > 0:
    for a in range(3):
      for b in range(3):
        func(x+n*a,y+n*b,n)

func(0,0,n)
for i in s:
  print(''.join(i))
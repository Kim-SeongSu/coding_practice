while True:
  B, N = map(int, input().split())
  
  if B==N==0:
    break
  
  x = int(B**(1/N))
  a, b, c = abs(B-(x-1)**N), abs(B-x**N), abs(B-(x+1)**N)
  min_ = min(a,b,c)
  print(x if min_ == b else x-1 if min_ == a else x+1)
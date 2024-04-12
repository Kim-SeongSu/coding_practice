for _ in range(int(input())):
  x1, y1, r1, x2, y2, r2 = map(int,input().split())
  d = ((x2-x1)**2 + (y2-y1)**2)**0.5
  if d == 0:
    print(0 if r1 != r2 else -1)
  else:
    if max([r1,r2,d]) == d:
      print(1 if r1+r2==d else 0 if d>r1+r2 else 2)
    else:
      if max([r1,r2,d]) == r1:
        print(1 if r2+d == r1 else 0 if r1>r2+d else 2)
      else:
        print(1 if r1+d == r2 else 0 if r2>r1+d else 2)
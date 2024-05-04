while True:
  ipt = int(input())
  if ipt == 0:
    break
  
  s, e = 1, 50
  while 1:
    m = s-1+(e-s+1)//2 if (e-s+1)%2==0 else s+(e-s+1)//2
    print(m, end=' ')
    if ipt == m:
      break
    elif ipt > m:
      s = m+1
    else:
      e = m-1
  print()
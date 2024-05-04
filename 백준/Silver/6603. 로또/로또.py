from itertools import combinations as cb

while True:
  n, *l = list(map(int,input().split()))
  if n == 0:
    break
  for i in list(cb(l,6)):
    print(*i)
  print()
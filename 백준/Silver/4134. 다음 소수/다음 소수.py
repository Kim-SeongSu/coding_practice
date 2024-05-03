def PrimeNum(n):
  x = 0
  while True:
    x = n
    for i in range(2,int(n**0.5)+1):
      if n % i == 0:
        n += 1
        break
    if x == n:
      return n

for _ in range(int(input())):
  n = int(input())
  print(2 if n < 3 else PrimeNum(n))
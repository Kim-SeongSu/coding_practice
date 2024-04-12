S = input()
x, l, arr = 1, len(S), []
while l > 0:
  for i in range(l):
    arr.append(S[i:i+x])
  l -= 1
  x += 1  
print(len(set(arr)))
ipt = input().split('-')
arr = []
for i in ipt:
  if '+' not in i:
    arr.append(str(int(i)))
  else:
    arr.append(str(sum([int(j) for j in i.split('+')])))
print(eval('-'.join(arr)))
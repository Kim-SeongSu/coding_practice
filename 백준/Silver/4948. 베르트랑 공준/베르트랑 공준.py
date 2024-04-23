n = 123456*2
arr = [0]+[1]*n
for i in range(2,int(n**(0.5))+1):
  if arr[i] == 1:
    for j in range(2*i,n+1,i):
      arr[j] = 0


while True:
  ipt = int(input())
  if ipt == 0:
    break
  print(sum(arr[ipt+1:2*ipt+1]))
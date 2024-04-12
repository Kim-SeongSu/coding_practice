x, y = map(int,input().split())
arr = [['*']*y, ['*']*x]

for _ in range(int(input())):
  cmd, l = map(int,input().split())
  arr[cmd][l] = ' *'

print(max(len(i) for i in ''.join(arr[0]).split())*max(len(i) for i in ''.join(arr[1]).split()))
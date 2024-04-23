'''
# 시간초과
A, B = map(int,input().split())
cnt = 1
while A < B:
  if str(B)[-1] == '1':
    B = int(str(B)[:-1])
  elif int(str(B)[-1])%2 == 0:
    B //= 2
  cnt += 1
print(cnt if A==B else -1) 
'''
A, B = map(int,input().split())
cnt = 1
while A<B:
  x = B
  if B%10 == 1:
    B //= 10 
  elif B%2 == 0:
    B //= 2
  
  if x == B:
    break
  cnt += 1
print(cnt if A==B else -1) 
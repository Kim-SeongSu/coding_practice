'''
# 시간초과
w, h = map(int,input().split())
p, q = map(int,input().split())

dx, dy = 1, 1
for _ in range(int(input())):
  if p+dx > w:
    dx = -1
  elif p+dx < 0:
    dx = 1
  if q+dy > h:
    dy = -1
  elif q+dy < 0:
    dy = 1
  p, q = p+dx, q+dy
print(p,q)
'''

w, h = map(int,input().split())
p, q = map(int,input().split())
t = int(input())

w_range = list(range(w+1))+list(range(w-1,-1,-1))
h_range = list(range(h+1))+list(range(h-1,-1,-1))
x, y = (t+p)%(2*w), (t+q)%(2*h)
print(w_range[x], h_range[y])
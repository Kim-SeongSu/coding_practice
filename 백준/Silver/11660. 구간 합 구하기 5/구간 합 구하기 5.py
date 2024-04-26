'''
# 시간초과
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]


for _ in range(M):
  x1, y1, x2, y2 = map(int,input().split())
  s = 0
  for i in range(x1-1,x2):
    for j in range(y1-1,y2):
      s += arr[i][j]
  print(s)
'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
S = [[0]*N for _ in range(N)]
for i in range(N):
  sum_ = 0
  temp = list(map(int,input().split()))
  for j in range(N):
    sum_ += temp[j]
    S[i][j] = sum_

for _ in range(M):
  x1, y1, x2, y2 = map(int,input().split())
  print(sum([S[i][y2-1] - S[i][y1-2] if y1 != 1 else S[i][y2-1] for i in range(x1-1,x2)]))
      
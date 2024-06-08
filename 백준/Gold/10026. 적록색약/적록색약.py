'''
# 메모리 초과
from collections import deque

N = int(input())
graph_1, graph_2 = [0]*N, [0]*N

for i in range(N):
  s = input()
  graph_1[i] = list(s) 
  graph_2[i] = list(s.replace('R','G'))

dx, dy = [0,0,1,-1], [1,-1,0,0]
q1, q2 = deque(), deque()

cnt1, cnt2 = 0, 0
for i in range(N):
  for j in range(N):
    if graph_1[i][j] != 'X':
      cnt1 += 1
      q1.append([i,j,graph_1[i][j]])
      while q1:
        x, y, k = q1.popleft()
        graph_1[x][y] = 'X'
        for n in range(4):
          nx, ny = x+dx[n], y+dy[n]
          if 0<=nx<N and 0<=ny<N and graph_1[nx][ny] == k:
            q1.append([nx,ny,k])

for i in range(N):
  for j in range(N):
    if graph_2[i][j] != 'X':
      cnt2 += 1
      q2.append([i,j,graph_2[i][j]])
      while q2:
        x, y, k = q2.popleft()
        graph_2[x][y] = 'X'
        for n in range(4):
          nx, ny = x+dx[n], y+dy[n]
          if 0<=nx<N and 0<=ny<N and graph_2[nx][ny] == k:
            q2.append([nx,ny,k])

print(cnt1, cnt2)
'''
# 재귀오류
import sys
sys.setrecursionlimit(10**4)

N = int(input())
graph = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

dx, dy = [0,0,1,-1], [1,-1,0,0]
cnt1, cnt2 = 0, 0

# 깊이 우선 탐색
def dfs(x,y):
    visited[x][y] = 1
    color = graph[x][y]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0<=nx<N) and (0<=ny<N):
            if (graph[nx][ny] == color) and (visited[nx][ny] == 0):
                dfs(nx,ny)

# R-G-B 탐색
for i in range(N):
    for j in range(N):
        if visited[i][j]==0:
            dfs(i,j)
            cnt1 += 1

# R-G 통합
for i in range(N):
    for j in range(N):
        if graph[i][j]=='G':
            graph[i][j]='R'

# visited 초기화
visited = [[0]*N for _ in range(N)]

# R-B 탐색
for i in range(N):
    for j in range(N):
        if visited[i][j]==0:
            dfs(i,j)
            cnt2 += 1

print(cnt1, cnt2)
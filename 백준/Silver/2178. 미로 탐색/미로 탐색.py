# BFS
from collections import deque

N, M = map(int,input().split())
graph = [list(map(int,input())) for _ in range(N)]
q = deque([(0,0)])

dx, dy = [0,0,1,-1], [1,-1,0,0]
cnt = 0

while q:
  x,y = q.popleft()
  for i in range(4):
    nx, ny = x+dx[i], y+dy[i]
    if (0 <= nx < N and 0 <= ny < M) and (graph[nx][ny] == 1):
      q.append((nx,ny))
      graph[nx][ny] = graph[x][y] + 1
print(graph[N-1][M-1])
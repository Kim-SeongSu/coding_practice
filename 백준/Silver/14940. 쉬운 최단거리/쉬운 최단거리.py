from collections import deque

N, M = map(int,input().split())
graph, q = [], deque()

for i in range(N):
  ipt = [i-2 for i in list(map(int,input().split()))]
  graph.append(ipt)
  if 0 in ipt:
    idx = ipt.index(0)
    q.append([i,idx])

dx,dy = [0,0,1,-1], [1,-1,0,0]
while q:
  x,y = q.popleft()
  for i in range(4):
    nx, ny = x+dx[i], y+dy[i]
    if (0<=nx<N and 0<=ny<M) and graph[nx][ny] == -1:
      q.append((nx,ny))
      graph[nx][ny] = graph[x][y] + 1

for row in graph:
  print(*[i if i!=-2 else 0 for i in row])
from collections import deque

M, N = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
q = deque()

for i in range(N):
  for j in range(M):
    if graph[i][j] == 1:
      q.append([i,j])

dx, dy = [0,0,1,-1], [1,-1,0,0]

while q:
  x, y = q.popleft()
  for i in range(4):
    nx, ny = x+dx[i], y+dy[i]
    if (0<=nx<N and 0<=ny<M) and graph[nx][ny] == 0:
      q.append([nx,ny])
      graph[nx][ny] = graph[x][y] + 1

ox, max_ = 1, 0
for i in graph:
  if 0 in i:
    ox = 0
    break  
  max_ = max(max_,max(i))
print(max_-1 if ox == 1 else -1)
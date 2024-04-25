from collections import deque

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
q = deque()
q.append([0,0])

ox = 0
while q:
  x, y = q.popleft()
  if graph[x][y] == -1:
    ox =1
    break
  if graph[x][y] == 0:
    continue
  j = graph[x][y]


  dx, dy = [0,j], [j,0]
  for i in range(2):
    nx, ny = x+dx[i], y+dy[i]
    if (0<=nx<N and 0<=ny<N):
      q.append([nx,ny])
print('HaruHaru' if ox==1 else 'Hing')
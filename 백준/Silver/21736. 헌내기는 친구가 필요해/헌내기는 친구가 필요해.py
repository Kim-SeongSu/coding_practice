from collections import deque

N, M = map(int,input().split())
graph, q = [], deque()

for i in range(N):
  ipt = list(input())
  graph.append(ipt)
  if 'I' in ipt:
    idx = ipt.index('I')
    q.append([i,idx])

    

dx,dy = [0,0,1,-1], [1,-1,0,0]
cnt = 0
while q:
  x,y = q.popleft()
  for i in range(4):
    nx, ny = x+dx[i], y+dy[i]
    if (0<=nx<N and 0<=ny<M) and graph[nx][ny] != 'X':
      q.append((nx,ny))
      if graph[nx][ny] == 'P':
        cnt += 1
      graph[nx][ny] = 'X'
      
print(cnt if cnt > 0 else 'TT')
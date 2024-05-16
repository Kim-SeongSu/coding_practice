N, M = map(int,input().split())
graph = [list(input()) for _ in range(N)]

def dfs(x,y,p):
  graph[x][y] = 'x'
  if (p == '-') and (y+1 < M) and (graph[x][y+1] == '-'):
    dfs(x,y+1,'-')
  elif (p == '|') and (x+1 < N) and (graph[x+1][y] == '|'):
    dfs(x+1,y,'|')
  else: return

cnt = 0
for i in range(N):
  for j in range(M):
    if graph[i][j] != 'x':
      cnt += 1
      dfs(i,j,graph[i][j])
      
print(cnt)
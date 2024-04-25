N, M = map(int,input().split())
if M == 0:
  print(N)
else:
  graph = [[] for _ in range(N+1)]
  total = []

  for _ in range(M):
    u, v = map(int,input().split())
    total += [u,v]
    graph[u].append(v)
    graph[v].append(u)

  total_num = len(set(total))

  def dfs(x):
    visited.append(x)
    for i in sorted(graph[x]):
      if i not in visited:
        dfs(i)

  cnt = 0
  while total != []:
    visited = []
    dfs(total[0])
    if visited != []:
      cnt += 1
      total = [i for i in total if i not in visited]
  print(cnt if N == total_num else N-total_num+cnt)
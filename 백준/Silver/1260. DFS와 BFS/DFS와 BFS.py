N, M, V = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

DFS_visited = []
BFS_visited = []


# DFS
def DFS(V):
  DFS_visited.append(V)
  for i in sorted(graph[V]):
    if i not in DFS_visited:
      DFS(i)


# BFS
def BFS(V):
  from collections import deque

  q = deque()
  q.append([V])

  while q:
    x = q.popleft()
    for i in x:
      if i not in BFS_visited:
        q.append(sorted(graph[i]))
        BFS_visited.append(i)
  return print(*BFS_visited)


DFS(V)
print(*DFS_visited)
BFS(V)
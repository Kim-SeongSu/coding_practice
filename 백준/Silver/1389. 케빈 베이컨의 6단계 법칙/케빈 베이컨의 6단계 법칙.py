# Floyd-Warshall (플로이드-워셜 알고리즘)
import sys

N, M = map(int,input().split())
INF = 999999
graph = [[INF]*N for _ in range(N)]

for i in range(N):
    graph[i][i] = 0

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1


for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = [[i,sum(x)] for i, x in enumerate(graph,1)]
print(sorted(result, key=lambda x: (x[1],x[0]))[0][0])
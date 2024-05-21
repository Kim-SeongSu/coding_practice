# Floyd-Warshall (플로이드-워셜 알고리즘)
import sys

N = int(input())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]


for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for x in graph:
    print(*x)
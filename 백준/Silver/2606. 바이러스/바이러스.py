# 그래프 알고리즘
'''
# BFS (너비 우선 탐색)
from collections import deque
import sys

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for _ in range(int(sys.stdin.readline())):
    a,b = sorted(map(int,sys.stdin.readline().split()))
    graph[a] += [b]
    graph[b] += [a]

Q = deque([1])
visited = [0,1]+[0]*(N-1)

while Q:
    x = Q.popleft()

    for i in graph[x]:
        if visited[i] == 0:
            Q.append(i)
            visited[i] = 1

print(visited[2:].count(1))
'''

# DFS (깊이 우선 탐색)
import sys

N = int(sys.stdin.readline())
V = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for _ in range(V):
    a,b = sorted(map(int,sys.stdin.readline().split()))
    graph[a] += [b]
    graph[b] += [a]

visited = [0]*(N+1)

def find_visited(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i]==0:
            find_visited(i)

find_visited(1)
print(visited[2:].count(1))
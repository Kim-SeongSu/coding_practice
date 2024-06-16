from collections import deque
import sys

sys.setrecursionlimit(10**4)

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

dx, dy = [-1,1,0,0], [0,0,-1,1]

def dfs(x,y,h):
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if (0<=nx<N) and (0<=ny<N):
            if (visited[nx][ny]==0) and (graph[nx][ny]>h):
                dfs(nx,ny,h)

safezone = 0
for h in range(101):
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if (visited[i][j]==0) and (graph[i][j]>h):
                dfs(i,j,h)
                cnt += 1
    safezone = max(safezone,cnt)
print(safezone)
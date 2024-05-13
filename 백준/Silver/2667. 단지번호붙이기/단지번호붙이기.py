from collections import deque

N = int(input())
graph = [list(map(int,list(input()))) for _ in range(N)]

dx, dy = [0,0,1,-1], [1,-1,0,0]

def bfs(N, i, j):
    q = deque([(i,j)])
    cnt = 1
    while q:
        x, y = q.popleft()
        graph[x][y] = 2

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < N and 0 <= ny < N) and (graph[nx][ny] == 1):
                q.append((nx,ny))
                graph[nx][ny] = 2
                cnt += 1
    return cnt

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            result.append(bfs(N,i,j))
print(len(result),*sorted(result), sep='\n')
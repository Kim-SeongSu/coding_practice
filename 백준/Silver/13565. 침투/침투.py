from collections import deque

M, N = map(int,input().split())
graph = [list(map(int,list(input()))) for _ in range(M)]

dx, dy = [0,0,1,-1], [1,-1,0,0]
q = deque([(0,i) for i in range(N)])

while q:
    x, y = q.popleft()
    if graph[x][y] == 0:
        graph[x][y] = 2

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < M and 0 <= ny < N) and (graph[nx][ny] == 0):
                q.append((nx,ny))

print('YES' if 2 in graph[-1] else 'NO')
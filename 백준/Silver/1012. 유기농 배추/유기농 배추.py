# 브루트 포스
import sys
## 재귀 한도(깊이) 제한 변경 함수 (default = 1000), 런타임 에러(RecursionError) 방지
sys.setrecursionlimit(10000) 

def BFS(x,y):
    plus_row, plus_col = [-1,1,0,0], [0,0,-1,1]

    for i in range(4):
        row, col = x+plus_row[i], y+plus_col[i]

        if  (-1 < row < N) and (-1 < col < M):
            if matrix[row][col] == 1:
                matrix[row][col] = -1
                BFS(row,col)


for _ in range(int(sys.stdin.readline())):
    M, N, K = map(int,sys.stdin.readline().split())
    matrix = [[0]*M for _ in range(N)]
    cnt = 0

    for i in range(K):
        X, Y = map(int,sys.stdin.readline().split())
        matrix[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                BFS(i,j)
                cnt += 1
    print(cnt)
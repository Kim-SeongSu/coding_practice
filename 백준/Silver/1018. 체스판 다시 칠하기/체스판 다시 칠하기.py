N,M = map(int,input().split())

board,chess = [0]*N, []

for i in range(N):
    board[i] = input()

for i in range(N-7):
    for j in range(M-7):
        white = 0
        black = 0
        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y) % 2 ==0:
                    if board[x][y] != 'W':
                        white += 1
                    else:
                        black += 1
                else:
                    if board[x][y] != 'W':
                        black += 1
                    else:
                        white += 1
        chess.append(white)
        chess.append(black)
print(min(chess))
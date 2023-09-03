def solution(board):
    n = len(board[0])
    arr=[['o']*(n+2) for i in range(n+2)]
    
    for i in range(n+2):
        for j in range(n+2):
            if i in [0,n+1] or j in [0,n+1]:
                arr[i][j] = 'x'
            
            else:
                if board[i-1][j-1] == 1:
                    for k in range(i-1,i+2):
                        for l in range(j-1,j+2):
                            arr[k][l] = 'x'
    return sum([(''.join(i)).count('o') for i in arr])
    
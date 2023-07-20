def solution(keyinput, board):
    answer,xmax,ymax,x,y = [],(board[0]-1)//2,(board[1]-1)//2,0,0
    
    for i in keyinput:
        if i == "left" and x > -xmax:x -= 1
        elif i == "right" and x < xmax:x += 1
        elif i == "down" and y > -ymax:y -= 1
        elif i == "up" and y < ymax:y += 1     
    return [x,y]
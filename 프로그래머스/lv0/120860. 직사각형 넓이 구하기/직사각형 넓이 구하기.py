def solution(dots):
    x = [x[0] for x in dots]
    y = [x[1] for x in dots]
    
    return (max(x)-min(x))*(max(y)-min(y))
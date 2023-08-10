def solution(n):
    x = ''
    while n > 0: 
        n,r = divmod(n,3)
        x += str(r)
    
    return int(x,3)
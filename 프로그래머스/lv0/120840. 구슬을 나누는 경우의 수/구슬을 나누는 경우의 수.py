def solution(balls, share):
    n,m = 1,1
    for i in range(share+1,balls+1):
        n *= i
    for i in range(1,balls-share+1):
        m *= i
    return n//m
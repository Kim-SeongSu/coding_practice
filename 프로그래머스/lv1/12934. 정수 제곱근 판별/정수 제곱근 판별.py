def solution(n):
    import math
    x = math.sqrt(n)
    return (x+1)**2 if int(x) == x else -1
def solution(n):    
    i = 1
    
    while n // i >= 1:
        n //= i
        i += 1
    return i-1
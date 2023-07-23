def solution(sides):
    a,b = max(sides), min(sides)
    
    R = [i for i in range(a-b+1,a+b)]
    return len(R) 
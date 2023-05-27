def solution(n):
    answer = 0
    Even, Odd = 0, 0
    
    for i in range(1,n+1):
        if i % 2 == 1:
            Odd += i
        else:
            Even += i**2  
            
    answer = Odd if n % 2 == 1 else Even
    return answer
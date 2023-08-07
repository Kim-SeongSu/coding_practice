def solution(left, right):
    result = 0
    for i in range(left,right+1):
        d,x,n = [],i,1
        
        while x >= n:
            if x % n == 0:
                d.append(n)
            n+=1  
            
        if len(set(d)) % 2 == 0: result += i
        else: result -= i
    return result
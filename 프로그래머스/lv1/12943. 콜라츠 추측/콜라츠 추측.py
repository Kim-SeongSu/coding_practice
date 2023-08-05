def solution(num):
    x = 0
    while num > 1:
        if num%2 ==0:
            num //= 2
        else:
            num *= 3
            num +=1
        x +=1
        
        if x > 500:
            return -1
            break
    return x
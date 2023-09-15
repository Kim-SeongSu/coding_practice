def div(n):
    c=0
    for i in range(1, int(n**(1/2)+1)):
            if n % i == 0:
                c += 1
                if i**2 != n:
                    c+=1    
    return c

def solution(number, limit, power):
    return sum([div(i) if div(i) <= limit else power for i in range(1,number+1)])
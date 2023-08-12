def solution(number):
    result = 0
    
    for i in range(n:=len(number)):
        for j in range(n):
            for k in range(n):
                if (i!=j!=k) and (i!=k) and (number[i]+number[j]+number[k] == 0):
                    result +=1
    return result//6
def solution(n): 
    x = n+1
    while format(n,'b').count('1') != format(x,'b').count('1'):x+=1
    return x
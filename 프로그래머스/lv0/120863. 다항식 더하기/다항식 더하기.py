def solution(polynomial):
    a,b = 0,0
    for i in polynomial.replace('+','').split():
        if i == 'x':
            a += 1
        elif i.endswith('x'):
            a += int(i[:-1])
        else:
            b += int(i)
    
    A,B = '',''
    if a==1:
        A = 'x'
    elif a>1:
        A = str(a)+'x'
        
    if b>0:
        B = str(b)
    
    
    return A+' + '+B if A!='' and B!='' else A if A != '' else B
        
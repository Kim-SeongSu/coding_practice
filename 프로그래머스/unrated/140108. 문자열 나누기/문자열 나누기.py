def solution(s):
    answer, x, xcount, ycount = 0, '', 0, 0
    for i in s:
        if x == '': x = i
        
        if i == x: xcount += 1
        else: ycount += 1
        
        if xcount == ycount:
            answer += 1
            x,xcount,ycount = '',0, 0
    
    return answer if xcount == 0 else answer + 1
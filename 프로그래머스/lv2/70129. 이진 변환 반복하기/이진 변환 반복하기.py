def solution(s):
    zero, counts = 0,0
    while s != '1':
        zero += sorted(list(s)).index('1')
        s = format(len(s.replace('0','')),'b')
        counts += 1
    
    return counts,zero
def solution(a, b, c, d):
    arr, L = [0]*6, [a,b,c,d]
    
    for i in L:
        arr[i-1] += 1
    
    if 4 in arr:
        return 1111 * a
    
    elif 3 in arr:
        p,q = arr.index(3)+1, arr.index(1)+1
        return (10*p+q)**2
    
    elif (2 in arr) & (len(set(L)) == 2):
        p,q = min(L),max(L)
        return (p+q)*(q-p)
    
    elif (2 in arr) & (len(set(L)) == 3):
        p,q,r = arr.index(2)+1, arr.index(1)+1, arr.index(1,(arr.index(1)+1))+1
        return q*r
    
    else:
        return min(L)
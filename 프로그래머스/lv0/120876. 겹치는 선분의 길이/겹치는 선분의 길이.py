def abc(a,b):
    arr = sorted([i for i in set(a+b) if (a+b).count(i) == 2])
    return arr if len(arr) > 1 else []

def solution(lines):
    a,b,c = [[j for j in range(i[0],i[1]+1)] for i in lines]
    
    arr = sorted(set(abc(a,b)+abc(b,c)+abc(c,a)))

    return sum([1 for i in range(len(arr)-1) if arr[i+1]-arr[i] == 1])

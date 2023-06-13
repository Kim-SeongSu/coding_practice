def solution(a, d, included):
    N = len(included)
    arr = list(range(a,a+d*(N-1)+1,d))
    result = 0
               
    for i in range(N):
        if included[i] == True:
               result += arr[i]
    return result
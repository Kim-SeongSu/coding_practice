def solution(n):
    arr = [0,1]
    for i in range(2,n+1):
        arr.append(arr[-1]+arr[-2])
    return arr[-1] % 1234567
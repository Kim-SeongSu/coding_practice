def solution(n):
    answer = 0
    for i in range(1,n+1):
        s,x = 0,i
        while s < n:
            s += x
            if s == n:
                answer += 1
            x += 1
    return answer
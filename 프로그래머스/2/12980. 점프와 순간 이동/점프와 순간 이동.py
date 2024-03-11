def solution(n):
    answer, x = 0, n
    if n % 2 != 0:
        answer = 1
        x -= 1
    
    while x != 0:
        x //= 2
        if x % 2 != 0:
            x -= 1
            answer += 1
    return answer
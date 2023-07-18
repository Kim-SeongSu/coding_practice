def solution(n):
    answer, x = [], 2
    while n >= x:
        if n % x == 0:
            n //= x
            answer.append(x)
        else: 
            x += 1
    return sorted(list(set(answer)))
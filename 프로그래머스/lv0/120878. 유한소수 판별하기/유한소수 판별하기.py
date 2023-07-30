def sol(n):
    x, result = 2, []
    while x <= n:
        if n % x == 0:
            n //= x
            result.append(x)
        else:
            x += 1
    return result
        

def solution(a, b):
    A,B = sol(a), sol(b)
    for i in A:
        if i in B:
            B.remove(i)
    if all(i in [5] for i in A):
        return 1
    return 1 if all(i in [2,5] for i in B) else 2
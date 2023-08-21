def solution(a, b, n):
    result, quotient, remainder = 0, 0, 0
    while n >= a:
        quotient, remainder = n//a*b, n%a
        n = quotient + remainder
        result += quotient
    return result
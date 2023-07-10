def solution(numbers, k):
    arr = numbers*(k)
    return arr[:2*k-1:2][-1]
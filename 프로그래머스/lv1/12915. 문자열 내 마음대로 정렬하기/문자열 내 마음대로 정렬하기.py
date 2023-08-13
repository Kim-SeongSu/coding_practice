def solution(strings, n):
    return [i[1:] for i in sorted([i[n]+i for i in strings])]
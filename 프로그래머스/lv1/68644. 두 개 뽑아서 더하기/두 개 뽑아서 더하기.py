def solution(numbers):
    import itertools as it
    return sorted(list(set([sum(i) for i in it.combinations(numbers,2)])))
def solution(d, budget):
    arr = sorted(d)
    while sum(arr) > budget:
        del arr[-1]
    return len(arr)
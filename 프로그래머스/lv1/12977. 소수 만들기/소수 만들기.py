def solution(nums):
    import itertools as it
    
    result = 0
    for i in [sum(i) for i in list(it.combinations(nums,3))]:
        temp = sum([0 if i % j != 0 else 1 for j in range(2,i+1)])
        if temp == 1: result += 1
    return result
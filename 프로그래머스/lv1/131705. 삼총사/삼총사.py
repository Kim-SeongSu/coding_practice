def solution(number):
    import itertools

    arr = [sum(i) for i in itertools.combinations(number,3) if sum(i) == 0]
          
    return len(arr)
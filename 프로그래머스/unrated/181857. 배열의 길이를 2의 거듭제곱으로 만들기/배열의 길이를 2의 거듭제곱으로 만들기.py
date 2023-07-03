def solution(arr):
    L = [(2)**i for i in range(11)]
    if len(arr) in L:
        return arr
    elif len(arr) == 0:
        return [0]
    else:
        for i in L:
            if i > len(arr):
                return arr+[0]*(i - len(arr))           
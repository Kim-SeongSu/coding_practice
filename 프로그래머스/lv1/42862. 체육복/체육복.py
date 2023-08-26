def solution(n, lost, reserve):
    n_lost = sorted([i for i in lost if i not in reserve])
    n_reserve = sorted([i for i in reserve if i not in lost])
    x = 0

    for i in n_lost:
        if i-1 in n_reserve:
            x += 1
            n_reserve.remove(i-1)
        
        elif i+1 in n_reserve:
            x += 1
            n_reserve.remove(i+1)
    return n-len(n_lost)+x
def solution(common):
    if common[1]-common[0] == common[-1]-common[-2]:
        return common[-1] + (common[1]-common[0])   
    elif common[1] // common[0] == common[-1] // common[-2]:
        return common[-1] * (common[1] // common[0])
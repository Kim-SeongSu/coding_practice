def solution(spell, dic):
    for i in dic:
        temp = 0
        for j in spell:
            if j in i:
                temp += 1
        if temp == len(spell):
            return 1
        
    return 2
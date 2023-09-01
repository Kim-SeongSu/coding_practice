def solution(ingredient):
    counts, temp = 0, []
    for i in ingredient:
        temp.append(i)
        if temp[-4:] == [1,2,3,1]:
            del temp[-4:]
            counts +=1        
    return counts
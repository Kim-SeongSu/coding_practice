def solution(absolutes, signs):
    result = 0
    for i in range(len(signs)):
        if signs[i] == True: m = 1
        else: m = -1     
        result += absolutes[i] * m
    return result
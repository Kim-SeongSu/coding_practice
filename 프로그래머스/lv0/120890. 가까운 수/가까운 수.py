def solution(array, n):
    S = [0]*len(array)
    
    for i in range(len(array)):
        S[i] = abs(sorted(array)[i] - n)

    return sorted(array)[S.index(min(S))]
def solution(n, words):
    arr = [words[0]]
    
    for i,v in enumerate(words[1:],1):
        if arr[-1][-1] == v[0] and v not in arr and len(v) > 1:
            arr.append(v)
        else:
            return i%n+1, i//n+1
    return [0,0]
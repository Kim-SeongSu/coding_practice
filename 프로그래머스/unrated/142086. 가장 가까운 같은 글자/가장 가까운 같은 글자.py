def solution(s):
    last, result = {}, []
    for i in range(len(s)):
        if s[i] not in list(last.keys()):
            last[s[i]] = i
            result.append(-1)
        else:
            result.append(i-last.get(s[i]))
            last[s[i]] = i
    
    return result
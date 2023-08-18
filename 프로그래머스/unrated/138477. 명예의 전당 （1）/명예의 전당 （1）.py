def solution(k, score):
    answer = []
    for i in range(len(score)):
        if i<k:
            s = sorted(score[:i+1])
        else:
            s = sorted(score[:i+1])[-k:] 
        answer.append(s[0])
            
    return answer
def solution(score):
    answer = []
    S = [E+M for E,M in score]
    for i in S: 
        counts = 1
        for j in S:
            if i < j: 
                counts += 1
        answer.append(counts)
    return answer
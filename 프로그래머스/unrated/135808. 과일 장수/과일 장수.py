def solution(k, m, score):
    return m*sum(sorted(score,reverse=True)[m-1::m][:len(score)//m])
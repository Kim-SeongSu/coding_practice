def solution(name, yearning, photo):
    score = {i:j for i,j in zip(name,yearning)}
       
    return [sum([score.get(j) if j in score.keys() else 0 for j in i]) for i in photo]
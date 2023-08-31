def solution(participant, completion):
    completion.append('zzzzzz')
    
    for x,y in zip(sorted(participant),sorted(completion)):
        if x != y:
            return x
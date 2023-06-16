def solution(emergency):
    index = list(range(1,len(emergency)+1))
    
    Dict = dict(zip(sorted(emergency,reverse=True),index))
    return [Dict.get(i) for i in emergency]
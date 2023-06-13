def solution(log):
    S = {1:'w',-1:'s',10:'d',-10:'a'}
    return ''.join([S.get(log[i+1]-log[i]) for i in range(len(log)-1)])
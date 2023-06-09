def solution(myString):
    S = myString.replace('x',',')
    return list(map(len,S.split(',')))
def solution(myString, pat):
    P = pat.replace('A','b').replace('B','a')
    return int(P.upper() in myString)
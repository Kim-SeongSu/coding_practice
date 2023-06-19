def solution(myString, pat):
    return myString[::-1][myString[::-1].find(pat[::-1]):][::-1]
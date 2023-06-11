def solution(myString):
    return list(filter(None,sorted(myString.replace('"','').split('x'))))
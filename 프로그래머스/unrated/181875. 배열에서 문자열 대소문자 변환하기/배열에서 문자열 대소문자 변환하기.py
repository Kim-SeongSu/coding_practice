def solution(strArr):
    return [i.lower() if strArr.index(i) % 2 == 0 else i.upper() for i in strArr]
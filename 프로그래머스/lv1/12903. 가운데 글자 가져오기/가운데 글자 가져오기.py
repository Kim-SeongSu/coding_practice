def solution(s):
    c = len(s)//2
    return s[c-1:c+1] if len(s) % 2 == 0 else s[c]
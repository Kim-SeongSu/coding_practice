def solution(s):
    if s[0] == ')': return False
    else:
        x = 0
        for i in s:
            if i == '(': x += 1
            else: x-=1
            if x <0: return False  
        return True if x == 0 else False
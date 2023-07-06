def solution(s):
    if 'l' in s or 'r' in s:
        for i in range(len(s)):
            if s[i] == 'r':
                s = s[i+1:]
                break
            elif s[i] == 'l' :
                s = s[:i]
                break
        return s
    else:
        return []
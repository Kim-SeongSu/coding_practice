def solution(s):
    answer, s = '', ' '+s
    
    for i in range(len(s)):
        if s[i].isdigit() or s[i] == ' ':
            answer += s[i]
        else:
            if s[i-1] == ' ':
                answer += s[i].upper()
            else:
                answer += s[i].lower()
                
    return answer[1:]    
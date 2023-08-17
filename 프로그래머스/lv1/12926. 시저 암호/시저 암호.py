def solution(s, n):
    answer = ''
    
    for i in s:
        if i == ' ': answer += ' '
        elif (i.islower() and ord(i)+n > 122) or (i.isupper() and ord(i)+n > 90): answer += chr(ord(i) + n - 26)
        else:answer += chr(ord(i)+n)
        
    return answer
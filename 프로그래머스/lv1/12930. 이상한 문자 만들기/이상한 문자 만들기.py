def solution(s):
    result, num = '', 0
    for i in s:
        if i == ' ':
            result += ' '
            num = 0
        elif num % 2 == 0:
            result += i.upper()
            num +=1
        else:
            result += i.lower()
            num +=1
    return result
def solution(my_string):
    answer = ''
    for i in list(my_string):
        answer += ' ' if i.isalpha() == True else i 
    
    return sum(map(int,answer.split()))
def solution(my_string):
    S = list(set(my_string))
    answer = [0]*52
    
    for i in S:
        n = my_string.count(i)
        if i.isupper() == True:
            answer[ord(i)-65] = n
        else:
            answer[ord(i)-71] = n
            
    return answer
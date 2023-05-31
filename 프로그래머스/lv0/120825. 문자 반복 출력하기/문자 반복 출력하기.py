def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += f'{i}'*n
    return answer
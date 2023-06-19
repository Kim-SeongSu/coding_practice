def solution(my_string, m, c):
    S = [my_string[i:i+m] for i in range(0, len(my_string), m)]
    return ''.join([S[i][c-1] for i in range(len(S))])
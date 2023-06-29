def solution(my_string, queries):
    S = list(my_string)
    for i in queries:
        S[i[0]:i[1]+1] = S[i[0]:i[1]+1][::-1]
    return ''.join(S)
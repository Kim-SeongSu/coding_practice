def solution(picture, k):
    result = []
    for i in picture: 
        row =''
        for j in i:
            row += j *k
        for _ in range(k):
            result.append(row)
    return result
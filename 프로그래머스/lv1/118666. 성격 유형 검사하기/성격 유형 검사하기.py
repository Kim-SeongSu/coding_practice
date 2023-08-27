def score(string,n):
    score = [3,2,1,0,1,2,3]
    a,b = 0,0
    if n < 4:
        a = score[n-1]
    elif n > 0:
        b = score[n-1]
    return a,b    


def solution(survey, choices):
    arr, counts = ['R','C','J','A','T','F','M','N'], [0]*8
    
    for i in range(len(survey)):
        a,b = score(survey[i],choices[i])
        counts[arr.index(survey[i][0])] += a
        counts[arr.index(survey[i][1])] += b
    
    answer = [arr[i] if counts[i] >= counts[i+4] else arr[i+4] for i in range(4)]     
        
    return ''.join(answer)
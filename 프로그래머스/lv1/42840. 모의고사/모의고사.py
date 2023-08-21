def solution(answers):
    arr,result = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]], []
    
    for i in arr:
        k = i*(1+len(answers)//len(i))
        result.append(sum([1 for j in range(len(answers)) if answers[j] == k[j]]))
    
    return [i for i,v in enumerate(result,1) if v == max(result)]
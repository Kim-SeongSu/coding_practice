def solution(arr, queries):
    result = []
    
    for i in queries:
        M = [j for j in arr[i[0]:i[1]+1] if j > i[2]]
        result.append(-1 if M == [] else sorted(M)[0])
    return result
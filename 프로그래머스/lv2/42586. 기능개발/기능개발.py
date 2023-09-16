def solution(p, s):
    std, index, arr = 0, 1, [(100-p[i])//s[i] if (100-p[i])%s[i] == 0 else (100-p[i])//s[i] +1 for i in range(len(p))]
    
    counts, answer = 1, []
    while index < len(arr):
        if arr[std] >= arr[index]:
            counts += 1
        else:
            answer.append(counts)
            std = index
            index = index 
            counts = 1
        index += 1
        if index == len(arr):
            answer.append(counts)  
    return  answer
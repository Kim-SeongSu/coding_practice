def solution(num_list, n):
    k = len(num_list) // n
    answer = []
    
    count = 0
    for _ in range(k):
        temp = []
        for _ in range(n):
            temp.append(num_list[count])
            count += 1
        answer.append(temp)
    
    return answer
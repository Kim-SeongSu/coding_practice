def solution(numlist, n):
    answer = []
    under,over = sorted([i for i in numlist if i<n]),sorted([i for i in numlist if i>=n])
    
    while under != [] and over != []:
        a = n - under[-1]
        b = over[0] - n
        
        if a>=b:
            answer.append(over[0])
            over = over[1:]
        else:
            answer.append(under[-1])
            under = under[:-1]
        
    return answer+over+under[::-1]
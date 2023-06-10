def solution(n):
    count = 0
    for i in range(1,n+1):
        if i % 2 == 0 and i != 2:
            count += 1
        elif i % 3 == 0 and i != 3:
            count += 1
        elif i % 5 == 0 and i != 5:
            count += 1
        elif i % 7 == 0 and i != 7:
            count += 1
    
    return count
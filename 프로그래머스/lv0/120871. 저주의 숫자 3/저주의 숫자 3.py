def solution(n):
    num, arr = 1, []
    for _ in range(n):
        if num %3 != 0 and '3' not in str(num):
            arr.append(num)
            num += 1
        else:
            while num %3 == 0 or '3' in str(num):
                num += 1
            arr.append(num)
            num += 1
        
    return arr[-1]
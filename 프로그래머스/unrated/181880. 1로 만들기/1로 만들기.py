def solution(num_list):
    count = 0
    for i in num_list:
        x = i
        while x > 1:
            x //= 2
            count += 1
    return count
def solution(num_list):
    temp = 1
    for i in num_list:
        temp *= i
    return int(temp < sum(num_list)**2)
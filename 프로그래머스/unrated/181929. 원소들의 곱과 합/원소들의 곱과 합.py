def solution(num_list):
    return int(eval('*'.join([str(i) for i in num_list])) < sum(num_list)**2)
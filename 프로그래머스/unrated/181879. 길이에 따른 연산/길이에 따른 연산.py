def solution(num_list):
    if len(num_list) > 10:
        return eval('+'.join(map(str,num_list)))
    else:
        return eval('*'.join(map(str,num_list)))
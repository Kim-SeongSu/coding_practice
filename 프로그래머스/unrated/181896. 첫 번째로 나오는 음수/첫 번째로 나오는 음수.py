def solution(num_list):
    while True:
        for i in num_list:
            if i < 0:
                return num_list.index(i)
                break
        return -1
        break
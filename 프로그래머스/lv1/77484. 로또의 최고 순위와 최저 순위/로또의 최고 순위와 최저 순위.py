def solution(lottos, win_nums):
    a = sum([1 if i in win_nums else 0 for i in lottos])
    b = lottos.count(0)
    result=[6,6,5,4,3,2,1]
    return result[a+b],result[a]
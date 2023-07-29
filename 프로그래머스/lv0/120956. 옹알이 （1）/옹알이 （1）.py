def solution(babbling):
    result =  ('.'.join(babbling).replace('aya','1').replace('ye','1').replace('woo','1').replace('ma','1')).split('.')
    return [i.isdigit() for i in result].count(True)
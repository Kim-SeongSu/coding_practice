def solution(order):
    import re
    result = re.sub('(3|6|9)','x',str(order))
    return result.count('x')
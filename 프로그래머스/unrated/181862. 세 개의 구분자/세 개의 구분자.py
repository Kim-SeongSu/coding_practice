def solution(myStr):
    import re
    result = re.sub('(a|b|c)',' ',myStr).split() 
    return result if result != [] else ["EMPTY"]
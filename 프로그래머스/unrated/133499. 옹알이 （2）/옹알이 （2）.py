def solution(babbling):
    import re
    temp = re.sub('(ayaaya|yeye|woowoo|mama)','×',','.join(babbling))
    result = re.sub('(aya|ye|woo|ma)','',temp)
    return result.split(',').count('')
def solution(n, arr1, arr2):
    import re
    return [re.sub('(1|2)','#',str(int(bin(arr1[i])[2:])+int(bin(arr2[i])[2:]))).rjust(n,'0').replace('0',' ') for i in range(n)]
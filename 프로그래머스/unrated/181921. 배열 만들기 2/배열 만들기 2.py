def solution(l, r):
    arr = [i for i in range(l,r+1) if i % 5 == 0 and (str(i).count('5') + str(i).count('0')) == len(str(i))]
    if arr == []:
        arr = [-1]
    return arr
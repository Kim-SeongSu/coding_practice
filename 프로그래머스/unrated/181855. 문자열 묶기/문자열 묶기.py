def solution(strArr):
    arr = [0]*len(strArr)
    for i in strArr:
        arr[len(i)] += 1
    return max(arr)
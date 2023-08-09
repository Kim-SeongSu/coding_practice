def solution(arr):
    result = [arr[0]]
    for i in arr:
        if i != result[-1]:
            result.append(i)
    return result
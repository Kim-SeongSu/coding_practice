def solution(my_string, indices):
    arr = list(my_string)
    for i in sorted(indices, reverse=True):
        del arr[i]
    return ''.join(arr)
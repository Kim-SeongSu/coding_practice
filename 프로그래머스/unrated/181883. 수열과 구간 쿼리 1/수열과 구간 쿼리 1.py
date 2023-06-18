def solution(arr, q):
    for i in range(len(q)):
        arr[q[i][0]:q[i][1]+1] = [j+1 for j in arr[q[i][0]:q[i][1]+1]]
    return arr



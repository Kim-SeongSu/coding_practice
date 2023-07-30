def solution(arr):
    count,temp = 0, [0]*len(arr)
    while temp != arr:
        if count != 0:
            arr = temp
            temp = [0]*len(arr)
        for i in range(len(arr)):
            if (arr[i] % 2 == 0) and (arr[i] >= 50):
                temp[i] = arr[i]//2
            elif (arr[i] % 2 != 0) and (arr[i] < 50):
                temp[i] = arr[i] * 2 + 1
            else:
                temp[i] = arr[i]   
        count += 1     
    return count -1
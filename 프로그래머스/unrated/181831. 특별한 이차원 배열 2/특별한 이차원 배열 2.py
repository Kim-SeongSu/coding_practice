def solution(arr):
    for i in range(n:=len(arr)):
        for j in range(n):
            if arr[i][j] != arr[j][i]:
                return 0        
                break
    return 1
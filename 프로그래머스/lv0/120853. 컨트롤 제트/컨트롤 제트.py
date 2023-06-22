def solution(s):
    arr = s.split()
    result = int(arr[0])
    
    for i in range(1,len(arr)):
        if arr[i] == 'Z':
            result -= int(arr[i-1])
        else:
            result += int(arr[i])
            
    return result
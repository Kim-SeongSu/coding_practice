def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        if answer == []:
            answer.append(arr[i])
        elif answer[-1] == arr[i]:
            del answer[-1]
        else:
            answer.append(arr[i])
    return answer if answer != [] else [-1]
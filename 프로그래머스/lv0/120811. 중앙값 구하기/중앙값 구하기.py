def solution(array):
    answer = sorted(array)
    return answer[(len(array)-1)//2]
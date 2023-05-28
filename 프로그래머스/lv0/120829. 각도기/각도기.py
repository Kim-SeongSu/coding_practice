def solution(angle):
    if angle == 90:
        answer = 2
    elif angle == 180: 
        answer = 4
    else:
        answer = 1 if (angle > 0) and (angle < 90) else 3
        
    return answer
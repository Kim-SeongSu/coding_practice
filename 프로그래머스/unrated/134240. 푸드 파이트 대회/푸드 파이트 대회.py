def solution(food):        
    arr = ''.join([str(i)*(food[i]//2) for i in range(1,len(food))])
    return arr+'0'+arr[::-1]
def solution(brown, yellow):
    a = [i for i in range(1,yellow+1) if yellow % i == 0]
    
    for i in range(len(a)):
        x,y = a[i], a[-i-1]
        if x+y == (brown-4)//2:
            return y+2,x+2
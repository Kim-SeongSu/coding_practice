def slope(a,b):
    return round((b[1]-a[1])/(b[0]-a[0]),2)

def solution(dots):
    return int(True in [slope(dots[0],dots[1])==slope(dots[2],dots[3]), slope(dots[0],dots[2]) == slope(dots[1],dots[3]),slope(dots[0],dots[3]) == slope(dots[1],dots[2])])
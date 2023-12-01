# 테스트는 통과하지만 0점??
def div(n1,n2):
    gcd, x = 1, 2
    while n1>=x and n2>=x:
        if n1%x == 0 and n2%x == 0:
            n1//=x
            n2//=x
            gcd*=x
        else:
            x+=1       
    return gcd*n1*n2


def solution(arr):
    lcm = arr[0]
    for i in range(1,len(arr)):
        if i == 1 or lcm == 1:
            lcm = max(lcm,i)
        lcm = div(lcm,arr[i])
    return lcm
def divisor(x):
    return [i for i in range(1,x+1) if x % i == 0]
            
def solution(n, m):
    divisor_n, divisor_m = divisor(n), divisor(m)
    GCD = max([i for i in divisor_m if i in divisor_n])
    return GCD, n*m//GCD
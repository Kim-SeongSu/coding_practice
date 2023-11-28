n = int(input())
def square(x):
    return sum([i**x for i in range(1,n+1)])
print(square(1), square(1)**2, square(3), sep='\n')
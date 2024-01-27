money = {'136 68':1000,'142 68':5000,'148 68':10000,'154 68':50000}

print(sum([money[input()] for _ in range(int(input()))]))
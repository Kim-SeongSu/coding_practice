n, x = int(input()), ''

for i in range(n):
    x = ' '*(n-i-1)+'*'
    if i == 0: 
        pass
    elif i == n-1:
        x += '*'*(2*n-2)
    else:
        x +=' '*(2*i-1)+'*'
    print(x)
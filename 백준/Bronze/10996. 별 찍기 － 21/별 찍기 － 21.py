n = int(input())

if n == 1:
    print('*')
else:
    x1, x2 = '', ''
    for i in range(1,n+1):
        if i % 2 != 0:
            x1 += '*'
            x2 += ' '
        else:
            x1 += ' '
            x2 += '*'

    for _ in range(n):
        print(x1,x2,sep='\n')
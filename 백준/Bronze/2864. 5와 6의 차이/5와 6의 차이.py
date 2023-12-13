def trans(x,n):
    if n == 5:
        return int(x.replace(str(n),'6'))
    else:
        return int(x.replace(str(n),'5'))
    
A, B = input().split()

x, y = trans(A,5)+trans(B,5), trans(A,6)+trans(B,6)
print(min(x,y), max(x,y))
A, B, C = input().split()

if A == B == C:
    print(f'{A}={B}={C}')
else:
    for i in ['+','-','*','/','==']: 
        for j in ['+','-','*','/','==']:
            if (eval(A+i+B+j+C) == True) & (i == '==' or j == '=='):
                print((A+i+B+j+C).replace('==','='))
                break
            else:
                pass
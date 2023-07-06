for _ in range(int(input())):
    arr = input()
    if arr[-1] == '(' or len(arr) %2 != 0: print('NO')
    else:
        A = arr.replace('(','+1').replace(')','-1')
        if eval(A) != 0: print('NO')
        else: 
            n, result = 0, ''

            for i in arr:
                if i == '(': n += 1
                else: n -=1
                    
                if n < 0:
                    result = 'NO'
            if result == 'NO': print(result)
            else: print('YES')
def solution(n):
    number = [i for i in range(n+1,n**2+1)]
    answer = [[0]*n for i in range(n)]
    answer[0] = list(range(1,n+1))
    
    x,y,l,c = list(range(1,n)),list(range(n)),n-1,1
    while l>0:
        if c%2==1:
            for i in x:
                answer[i][y[-1]] = number[0]
                del number[0]
            del y[-1]
            for i in y[::-1]:
                answer[x[-1]][i] =number[0]
                del number[0]
            del x[-1]
        else:
            for i in x[::-1]:
                answer[i][y[0]] = number[0]
                del number[0]
            del y[0]
            for i in y:
                answer[x[0]][i] =number[0]
                del number[0]
            del x[0]
        c+=1
        l-=1
    return answer
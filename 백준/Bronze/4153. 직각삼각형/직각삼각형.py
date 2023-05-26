while True:
    N = list(map(int,input().split()))
    
    if N == [0,0,0]:
        break
    
    N.remove(MaxN:= max(N))

    if len(N) <= 1:
        print('worng')
    
    print('right' if MaxN**2 == N[0]**2 + N[1]**2 else 'wrong')
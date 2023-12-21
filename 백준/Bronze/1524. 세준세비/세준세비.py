for _ in range(int(input())):
    input()
    N, M = map(int,input().split())
    SJ = sorted(map(int,input().split()))
    SB = sorted(map(int,input().split()))
    
    while SJ != [] and SB!= []:
        if SJ[0] < SB[0]:
            del SJ[0]
        else:
            del SB[0]
        
    print('S' if SB == [] and SJ != [] else 'C' if SB == [] and SJ == [] else 'B')
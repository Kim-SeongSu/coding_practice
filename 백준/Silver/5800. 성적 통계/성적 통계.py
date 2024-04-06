for i in range(1,int(input())+1):
    N, *scores = map(int,input().split())
    S = sorted(scores)
    gap = 0
    for x in range(1,N):
        gap = max(gap, S[x]-S[x-1])
    print(f'Class {i}')
    print(f'Max {S[-1]}, Min {S[0]}, Largest gap {gap}')
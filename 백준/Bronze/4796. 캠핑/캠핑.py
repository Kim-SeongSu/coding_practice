cnt = 0
while 1:
    L, P, V = map(int,input().split())
    cnt += 1
    if L == P == V == 0:
        break
    
    print(f'Case {cnt}: {L*(V//P) + min(L,V%P)}')
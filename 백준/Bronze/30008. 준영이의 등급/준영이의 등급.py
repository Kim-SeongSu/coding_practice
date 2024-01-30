N, K = map(int,input().split())
score = [0]*K

cnt = 0
for i in list(map(int,input().split())):
    P = i*100//N

    if P > 96:
        score[cnt] = 9
    elif P > 89:
        score[cnt] = 8
    elif P > 77:
        score[cnt] = 7
    elif P > 60:
        score[cnt] = 6
    elif P > 40:
        score[cnt] = 5
    elif P > 23:
        score[cnt] = 4
    elif P > 11:
        score[cnt] = 3
    elif P > 4:
        score[cnt] = 2
    else:
        score[cnt] = 1
    cnt += 1
print(*score)
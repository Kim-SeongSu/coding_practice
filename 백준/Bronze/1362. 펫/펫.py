import sys

cnt = 0
while True:
    x = sys.stdin.readline().strip()

    if x == '0 0':
        break

    if x[0].isdigit():
        o, w = map(int,x.split())
        Min, Max, emotion = 0.5*o, 2*o, ''
        cnt += 1

        while True:
            order, n = sys.stdin.readline().split()
            if order == '#': 
                break
            if w < 1: 
                pass
            else:
                if order == 'F': 
                    w += int(n)
                else: 
                    w -= int(n)
    
        if w < 1: emotion = 'RIP';
        elif Min < w < Max: emotion = ':-)';
        else: emotion = ':-(';

        print(cnt, emotion)   
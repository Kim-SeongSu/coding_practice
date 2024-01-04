answer = {'Q1':0, 'Q2':0, 'Q3':0, 'Q4':0, 'AXIS':0, }

for _ in range(int(input())):
    x, y = map(int,input().split())
    if x == 0 or y == 0:
        answer['AXIS'] += 1
    else:
        if x > 0:
            if y > 0:
                answer['Q1'] += 1
            else:
                answer['Q4'] += 1
        else:
            if y > 0:
                answer['Q2'] += 1
            else:
                answer['Q3'] += 1            

for idx in answer:
    print(f'{idx}: {answer[idx]}')
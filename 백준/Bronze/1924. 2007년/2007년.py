month = {'1':31,'2':28,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31}

M, D = map(int,input().split())
if M == 1:
    days = D
else:
    days = sum([month[str(i)] for i in range(1,M)])+D
print(['SUN','MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'][days%7])
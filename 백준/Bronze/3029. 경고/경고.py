from datetime import datetime

x = datetime.strptime(input(),'%H:%M:%S')
y = datetime.strptime(input(),'%H:%M:%S')
if x == y:
    print('24:00:00')
else:
    print(str(y-x)[-8:].lstrip() if len(str(y-x)[-8:].lstrip()) == 8 else '0'+str(y-x)[-8:].lstrip())
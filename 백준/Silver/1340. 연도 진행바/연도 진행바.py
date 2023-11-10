import sys
from datetime import datetime

# +참고할 점) 한자리 숫자 앞에 0 안넣어도 자동으로 채워서 인식함
# Month = {'January':'01','February':'02', 'March':'03', 'April':'04', 'May':'05', 'June':'06', 'July':'07', 'August':'08', 'September':'09', 'October':'10', 'November':'11', 'December':'12'}
a,b = map(str,sys.stdin.readline().split(','))

# month, day, year, hour, minute = Month[a.split()[0]], a.split()[1], b.split()[0], b.split()[1][:2], b.split()[1][3:]
# %B는 영어로 된 월 문자열 (참고로 %A는 영어로 된 요일 문자열)
month, day, year, hour, minute = a.split()[0], a.split()[1], b.split()[0], b.split()[1][:2], b.split()[1][3:]

X = datetime.strptime(f'{year}-{month}-{day} {hour}:{minute}', '%Y-%B-%d %H:%M')
start, end = datetime.strptime(f'{year}-01-01 00:00', '%Y-%m-%d %H:%M'), datetime.strptime(f'{str(int(year)+1)}-01-01 00:00', '%Y-%m-%d %H:%M')

print(100*((X-start).total_seconds()/60) / ((end-start).total_seconds()/60))
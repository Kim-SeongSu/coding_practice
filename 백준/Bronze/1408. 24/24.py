from datetime import datetime 

tn = datetime.strptime(input(),'%H:%M:%S')
ts = datetime.strptime(input(),'%H:%M:%S')
time_24 = datetime.strptime('23:59:59','%H:%M:%S')


x = (ts-tn).seconds if ts>tn else 60*60*24-(tn-ts).seconds

h,m,s = x//3600,x%3600//60,x%60
print(':'.join([str(format(h,'02')),str(format(m,'02')),str(format(s,'02'))]))
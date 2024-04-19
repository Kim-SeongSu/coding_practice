import re

l = re.sub('[a-z]','',input()).replace(' ','')

x=0
for i in l:
    if i == 'UCPC'[x]:
        x += 1
        if x == 4:
            break
print('I love UCPC' if x == 4 else 'I hate UCPC')
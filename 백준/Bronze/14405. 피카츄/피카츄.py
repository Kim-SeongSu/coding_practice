import re

print('YES' if re.sub('pi|ka|chu','',input()) == '' else 'NO')
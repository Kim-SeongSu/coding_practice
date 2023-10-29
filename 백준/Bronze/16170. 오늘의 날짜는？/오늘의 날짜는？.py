import time

now = time.gmtime(time.time())
print(now.tm_year, now.tm_mon, now.tm_mday, sep='\n')
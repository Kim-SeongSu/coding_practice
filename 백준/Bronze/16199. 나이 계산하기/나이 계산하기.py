byear, bmonth, bday = map(int,input().split())
year, month, day = map(int,input().split())

print(year-byear if (month > bmonth) or (month == bmonth and day >= bday) else year-byear-1)
print(year-byear+1)
print(year-byear)
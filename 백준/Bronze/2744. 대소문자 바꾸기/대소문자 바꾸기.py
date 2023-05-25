result = ''

for i in input():
    result += i.lower() if i.isupper() else i.upper()

print(result)
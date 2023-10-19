import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s == '# 0 0':
        break
    
    name, age, weight = s.split()
    print(f'{name} Junior' if int(age) < 18 and int(weight) < 80 else f'{name} Senior')
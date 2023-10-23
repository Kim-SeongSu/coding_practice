import sys

strings = []

while True:
    S = sys.stdin.readline()
    if S =='':
        break
    else:
        strings.append(S.strip())

for i in strings:
    print(i)
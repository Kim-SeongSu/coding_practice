'''
'A' = 65  ~  'Z' = 90
'a' = 97  ~  'z' = 122

'''
import sys

ROT13, x = '', ''
for i in sys.stdin.readline().rstrip():
    if i.isalpha() == 1:
        if i.islower() == 1:
            x = chr(ord(i)+13) if ord(i) < 110 else chr(ord(i)-13)
        else:
            x = chr(ord(i)+13) if ord(i) < 78 else chr(ord(i)-13)
    else:
        x = i
    ROT13 += x
print(ROT13)
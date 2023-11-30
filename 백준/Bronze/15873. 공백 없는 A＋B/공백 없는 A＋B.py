n = input()
if len(n) == 2:
    print(int(n[0]) + int(n[1]))
elif n == '1010':
    print(20)
else:
    if int(n[1]) == 0:
        print(10 + int(n[2]))
    else:
        print(int(n[0]) + 10)
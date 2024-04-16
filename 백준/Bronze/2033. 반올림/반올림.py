N, x = input(), 0
for i in N[::-1][:-1]:
    num = int(i)+x
    if num < 5:
        x = 0
    else:
        x = 1
print((int(N[0])+x)*(10**(len(N)-1)))
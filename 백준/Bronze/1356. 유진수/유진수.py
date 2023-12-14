N, x = input(), 0

for i in range(1,len(N)):
    if eval('*'.join(N[:i])) == eval('*'.join(N[i:])):
        x = 1
        break
print('YES' if x == 1 and int(N) > 9 else 'NO')
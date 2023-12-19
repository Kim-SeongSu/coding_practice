X, Y = 0,0
for _ in range(int(input())):
    s = input()
    if s == 'D':
        X += 1
    else:
        Y += 1
    if abs(X-Y) > 1:
        break
print(f'{X}:{Y}')
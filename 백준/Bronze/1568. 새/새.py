N, x, cnt = int(input()), 1, 0
while N > 0:
    if N >= x:
        N -= x
    else:
        x = 1
        N -= x
    x += 1
    cnt += 1
print(cnt)
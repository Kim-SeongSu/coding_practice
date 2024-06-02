n = 1;
while 1:
    ipt = int(input())
    if ipt == 0:
        break
    else:
        print(f'{n}. odd {ipt//2}' if ipt%2==1 else f'{n}. even {ipt//2}')
        n += 1
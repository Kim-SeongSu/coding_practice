for _ in range(int(input())):
    r, e, c = map(int,input().split())
    print('advertise' if r+c < e else 'does not matter' if r+c == e else'do not advertise')
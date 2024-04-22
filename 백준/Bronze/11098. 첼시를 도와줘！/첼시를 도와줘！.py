for _ in range(int(input())):
    c = {}
    for _ in range(int(input())):
        price, player = input().split()
        c[price] = player
    print(c[sorted(c, key=lambda x: int(x), reverse=True)[0]])  
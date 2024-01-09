for _ in range(int(input())):
    a, b = map(int,input().split())
    x = 0
    if a == 0:
        x += 0
    elif a < 2:
        x += 5000000
    elif a < 4:
        x += 3000000
    elif a < 7:
        x += 2000000
    elif a < 11:
        x += 500000
    elif a < 16:
        x += 300000
    elif a < 22:
        x += 100000

    if b == 0:
        x += 0
    elif b < 2:
        x += 5120000
    elif b < 4:
        x += 2560000
    elif b < 8:
        x += 1280000
    elif b < 16:
        x += 640000
    elif b < 32:
        x += 320000
    
    print(x)
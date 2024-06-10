a, b, c, d = 6, 2, 3, 4

while a < 101:
    for i in range(b,a):
        for j in range(c,a):
            for k in range(d,a):
                if i<j<k and a**3 == i**3 + j**3 + k**3:
                    print(f'Cube = {a}, Triple = ({i},{j},{k})')
                    continue
    a += 1
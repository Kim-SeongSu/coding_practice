for _ in range(int(input())):
    C, G = 0, 0
    for _ in range(int(input())):
        a, b = input().split()
        C += int(a)
        G += float(b)*int(a)
    print(C, f'{G/C:.1f}', sep=' ')